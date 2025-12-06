# 1. Put access.log.txt into a sqlite db
# 2. Extract data from db and make a website geographic viz
# 3. Read db into a pandas df and make 4 vizzes

import re
import sqlite3
import time
from datetime import datetime

import folium
import pandas as pd
import requests


def parse_apache_log_line(log_line):
    pattern = (
        r"^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # IP address
        r" (\S+)"  # Identity
        r" (\S+)"  # User ID
        r" \[([^\]]+)\]"  # Timestamp
        r' "([^"]*(?:\\.[^"]*)*)"'  # Request line
        r" (\d{3})"  # Status code
        r" (\d+|-)"  # Response size
        r' "([^"]*(?:\\.[^"]*)*)"'  # Referrer
        r' "([^"]*(?:\\.[^"]*)*)"$'  # User agent
    )

    match = re.match(pattern, log_line)

    if not match:
        return None

    # Parse the request line separately
    request_line = match.group(5)
    request_parts = request_line.split(" ", 2)

    if len(request_parts) == 3:
        http_method, request_path, protocol_version = request_parts
    elif len(request_parts) == 2:
        http_method, request_path = request_parts
        protocol_version = None
    elif len(request_parts) == 1 and request_parts[0]:
        http_method = request_parts[0]
        request_path = None
        protocol_version = None
    else:
        http_method = None
        request_path = None
        protocol_version = None

    response_size = match.group(7)

    return {
        "ip_address": match.group(1),
        "identity": match.group(2),
        "user_id": match.group(3),
        "timestamp": format_timestamp(match.group(4)),
        "http_method": http_method,
        "request_path": request_path,
        "protocol_version": protocol_version,
        "status_code": int(match.group(6)),
        "response_size": int(response_size) if response_size != "-" else 0,
        "referrer": match.group(8),
        "user_agent": match.group(9),
    }


def format_timestamp(time_stamp):
    # Current format: 18/Jul/2011:05:13:51 -0500
    dt = datetime.strptime(time_stamp, "%d/%b/%Y:%H:%M:%S %z")
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def load_file_to_db():
    conn = sqlite3.connect("web_server_access_logs.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Logs")

    cur.execute("""
        CREATE TABLE Logs (
            ip_address TEXT,
            identity TEXT,
            user_id TEXT,
            timestamp INTEGER,
            http_method TEXT,
            request_path TEXT,
            protocol_version TEXT,
            status_code INTEGER,
            response_size INTEGER,
            referrer TEXT,
            user_agent TEXT
        )
    """)

    fh = open("access.log.txt")
    for line in fh:
        log_line_parsed = parse_apache_log_line(line)

        cur.execute(
            """INSERT INTO Logs VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                log_line_parsed["ip_address"],
                log_line_parsed["identity"],
                log_line_parsed["user_id"],
                log_line_parsed["timestamp"],
                log_line_parsed["http_method"],
                log_line_parsed["request_path"],
                log_line_parsed["protocol_version"],
                log_line_parsed["status_code"],
                log_line_parsed["response_size"],
                log_line_parsed["referrer"],
                log_line_parsed["user_agent"],
            ),
        )

    conn.commit()
    cur.close()
    fh.close()
    conn.close()


def geolocate_ip_batch(ip_list, max_retries=3):
    """Geolocate up to 100 IPs in a single batch request."""
    BATCH_API_URL = "http://ip-api.com/batch"

    # Build request payload with fields we need
    payload = [
        {"query": ip, "fields": "query,status,lat,lon,city,country"}
        for ip in ip_list
    ]

    for attempt in range(max_retries):
        try:
            response = requests.post(BATCH_API_URL, json=payload, timeout=30)

            if response.status_code == 429:
                wait_time = 2**attempt * 10
                print(f"Rate limit hit. Waiting {wait_time}s...")
                time.sleep(wait_time)
                continue

            data = response.json()
            results = {}

            for item in data:
                ip = item.get("query")
                if item.get("status") == "success":
                    results[ip] = {
                        "lat": item["lat"],
                        "lon": item["lon"],
                        "city": item.get("city", "N/A"),
                        "country": item.get("country", "N/A"),
                    }
                else:
                    results[ip] = None

            return results

        except requests.exceptions.RequestException as e:
            print(f"Request error: {e}. Retrying...")
            time.sleep(2**attempt * 5)

    return {}


def extract_ip_addresses_and_output_map():
    OUTPUT_MAP_FILE = "ip_origins_map.html"
    BATCH_SIZE = 100  # Max IPs per batch request
    IP_LIMIT = 5000  # Total IPs to process

    conn = sqlite3.connect("web_server_access_logs.sqlite")
    try:
        df = pd.read_sql_query(
            f"SELECT ip_address, COUNT(*) as request_count FROM Logs GROUP BY ip_address ORDER BY request_count DESC LIMIT {IP_LIMIT}",
            conn,
        )

        print(f"Processing {len(df)} unique IPs using batch API...")

        ip_locations = {}
        all_locations_data = []

        # Process IPs in batches of 100
        ip_list = df["ip_address"].tolist()
        request_counts = dict(zip(df["ip_address"], df["request_count"]))

        for i in range(0, len(ip_list), BATCH_SIZE):
            batch = ip_list[i : i + BATCH_SIZE]
            batch_num = i // BATCH_SIZE + 1
            total_batches = (len(ip_list) + BATCH_SIZE - 1) // BATCH_SIZE

            print(
                f"Processing batch {batch_num}/{total_batches} ({len(batch)} IPs)..."
            )

            batch_results = geolocate_ip_batch(batch)
            ip_locations.update(batch_results)

            # Add to all_locations_data with request counts
            for ip, loc_data in batch_results.items():
                if loc_data:
                    loc = loc_data.copy()
                    loc["request_count"] = request_counts[ip]
                    all_locations_data.append(loc)

            # Rate limit: 15 requests per minute = 4 seconds between batches
            if i + BATCH_SIZE < len(ip_list):
                time.sleep(4)

        # Generate map
        if not all_locations_data:
            print("No valid IPs found.")
            return

        # Aggregate request counts by location
        location_requests = {}
        for loc in all_locations_data:
            key = (loc["lat"], loc["lon"])
            if key not in location_requests:
                location_requests[key] = {
                    "city": loc["city"],
                    "country": loc["country"],
                    "total_requests": 0,
                }
            location_requests[key]["total_requests"] += loc["request_count"]

        max_requests = max(
            info["total_requests"] for info in location_requests.values()
        )

        m = folium.Map(location=[20, 0], zoom_start=2)

        for (lat, lon), info in location_requests.items():
            city = info["city"]
            country = info["country"]
            total_requests = info["total_requests"]

            radius = 5 + (total_requests * 20 / max_requests)

            popup_html = f"""
                <strong>Location:</strong> {city}, {country}<br>
                <strong>Requests:</strong> {total_requests}<br>
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
        print(f"Map saved to: {OUTPUT_MAP_FILE}")

    finally:
        conn.close()


def create_data_visualizations():
    pass


if __name__ == "__main__":
    # load_file_to_db()

    # This method will take a bit to process. It will process 5000 ip_addresses in batches of 100.
    # Uncomment if you want to run it yourself!
    # extract_ip_addresses_and_output_map()

    create_data_visualizations()
