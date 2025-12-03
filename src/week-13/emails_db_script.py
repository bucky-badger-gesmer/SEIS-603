# STEP 1: Import required libraries
import mailbox
import re
import socket
import sqlite3
import time
from collections import Counter
from email.utils import parsedate_to_datetime

import dns.resolver
import folium
import requests

# STEP 2: Configuration
MBOX_FILENAME = "mbox.txt"
OUTPUT_MAP_FILE = "email_origins_map.html"
DB_FILE = "emails.db"
GEOLOCATION_API_URL = "http://ip-api.com/json/"
IP_REGEX = re.compile(r"\[(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\]")


# STEP 3: Initialize SQLite database
def init_database():
    # Create a SQLite table to store results
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS email_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender_ip TEXT,
            domain TEXT,
            lat REAL,
            lon REAL,
            city TEXT,
            country TEXT,
            timestamp TEXT,
            source_file TEXT,
            email_index INTEGER
        )
    """)
    conn.commit()
    return conn


# STEP 4: Save extracted info into SQLite
def save_to_database(conn, ip, domain, loc, timestamp, index):
    cur = conn.cursor()
    cur.execute(
        """
        INSERT INTO email_data(sender_ip, domain, lat, lon, city, country, timestamp, source_file, email_index)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
        (
            ip,
            domain,
            loc["lat"],
            loc["lon"],
            loc["city"],
            loc["country"],
            timestamp,
            MBOX_FILENAME,
            index,
        ),
    )
    conn.commit()


# STEP 5: Extract the domain from the From: header
def extract_domain_from_email(message):
    from_header = message.get("From")
    if not from_header:
        return None

    match = re.search(r"<([^>]+)>", from_header)
    if match:
        email = match.group(1)
    else:
        match = re.search(r"([\w\.-]+@[\w\.-]+)", from_header)
        if not match:
            return None
        email = match.group(1)

    domain_match = re.search(r"@([\w\.-]+)$", email)
    if domain_match:
        return domain_match.group(1)

    return None


# STEP 6: Detect private IP addresses
def is_private_ip(ip):
    return ip.startswith(
        (
            "10.",
            "192.168.",
            "172.16.",
            "172.17.",
            "172.18.",
            "172.19.",
            "172.2",
            "172.3",
            "127.0",
        )
    )


# STEP 7: Resolve a domain to an IP using DNS
def resolve_domain_ip(domain):
    try:
        ip = socket.gethostbyname(domain)
        if not is_private_ip(ip):
            return ip
    except Exception:
        pass

    try:
        answers = dns.resolver.resolve(domain, "MX")
        for rdata in answers:
            mx_host = str(rdata.exchange).rstrip(".")
            try:
                ip = socket.gethostbyname(mx_host)
                if not is_private_ip(ip):
                    return ip
            except Exception:
                continue
    except Exception:
        pass

    return None


# STEP 8: Extract sender IP or fall back to DNS
def get_sender_ip(message):
    received_headers = message.get_all("Received")

    if received_headers:
        for header in reversed(received_headers):
            match = IP_REGEX.search(header)
            if match:
                ip_address = match.group(1)
                if not is_private_ip(ip_address):
                    return ip_address

    domain = extract_domain_from_email(message)
    if domain:
        dns_ip = resolve_domain_ip(domain)
        if dns_ip:
            print(f"DNS fallback: {domain} -> {dns_ip}")
            return dns_ip

    return None


# STEP 9: Extract timestamp from Date: header
def extract_timestamp(message):
    date_header = message.get("Date")
    if not date_header:
        return None
    try:
        dt = parsedate_to_datetime(date_header)
        return dt.isoformat()
    except Exception:
        return None


# STEP 10: Geolocate IP address
def geolocate_ip(ip_address, max_retries=3):
    for attempt in range(max_retries):
        try:
            url = f"{GEOLOCATION_API_URL}{ip_address}?fields=lat,lon,city,country,status,message"
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            data = response.json()

            if data.get("status") == "success":
                return {
                    "lat": data["lat"],
                    "lon": data["lon"],
                    "city": data.get("city", "N/A"),
                    "country": data.get("country", "N/A"),
                }

            if data.get("message") and "limit" in data["message"].lower():
                print(f"RATE LIMIT HIT for {ip_address}. Waiting...")
                time.sleep(2**attempt * 5)
                continue

            return None

        except requests.exceptions.RequestException:
            time.sleep(2**attempt)

    return None


# STEP 11: Parse mailbox, geolocate IPs, save data, and map results
def parse_mbox_and_plot():
    conn = init_database()

    try:
        mbox = mailbox.mbox(MBOX_FILENAME)
    except Exception as e:
        print(f"ERROR opening mbox: {e}")
        return

    print(f"--- Processing {len(mbox)} emails from {MBOX_FILENAME} ---")

    ip_locations = {}
    all_locations_data = []

    for i, message in enumerate(mbox):
        if i % 100 == 0 and i > 0:
            print(f"Processed {i} emails...")

        ip = get_sender_ip(message)
        domain = extract_domain_from_email(message)
        timestamp = extract_timestamp(message)

        if ip and ip not in ip_locations:
            location_data = geolocate_ip(ip)

            if location_data:
                ip_locations[ip] = location_data
                print(
                    f"Geolocated {ip} -> {location_data.get('city')}, {location_data.get('country')}"
                )
                time.sleep(1)
            else:
                ip_locations[ip] = None

        if ip and ip_locations.get(ip):
            all_locations_data.append(ip_locations[ip])
            save_to_database(conn, ip, domain, ip_locations[ip], timestamp, i)

    conn.close()

    print("--- Finished IP Extraction, Geolocation, and Database Save ---")

    if not all_locations_data:
        print("No valid IPs found.")
        return

    location_counts = Counter(
        (loc["lat"], loc["lon"]) for loc in all_locations_data
    )

    print(f"--- Generating Map: {OUTPUT_MAP_FILE} ---")
    m = folium.Map(location=[20, 0], zoom_start=2)

    for (lat, lon), count in location_counts.items():
        location_info = next(
            loc
            for loc in all_locations_data
            if loc["lat"] == lat and loc["lon"] == lon
        )
        city = location_info["city"]
        country = location_info["country"]

        radius = 5 + (count * 20 / max(location_counts.values()))

        popup_html = f"""
            <strong>Location:</strong> {city}, {country}<br>
            <strong>Emails:</strong> {count}<br>
            <strong>Coordinates:</strong> {lat:.4f}, {lon:.4f}
        """

        folium.CircleMarker(
            location=[lat, lon],
            radius=radius,
            popup=popup_html,
            color="#E53935",
            fill=True,
            fill_color="#FF5722",
            fill_opacity=0.7,
        ).add_to(m)

    m.save(OUTPUT_MAP_FILE)
    print(f"SUCCESS! Map saved to: {OUTPUT_MAP_FILE}")


# STEP 12: Run the program
if __name__ == "__main__":
    parse_mbox_and_plot()
