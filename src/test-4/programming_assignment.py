# 1. Put access.log.txt into a sqlite db
# 2. Extract data from db and make a website geographic viz
# 3. Read db into a pandas df and make 4 vizzes

import re
import sqlite3
from datetime import datetime


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


if __name__ == "__main__":
    load_file_to_db()
