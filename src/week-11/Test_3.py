import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("time.nist.gov", 13))
data = s.recv(512)
print(data.decode())

s.close()


# import logging
# from typing import Any

# import requests

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
# )


# def fetch_breweries(city: str) -> list[dict[str, Any]]:
#     """Fetch breweries by city and return JSON data."""
#     url = f"https://api.openbrewerydb.org/v1/breweries?by_city={city}"

#     try:
#         logging.info(f"Requesting data from {url}")
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()

#         data = response.json()
#         if not isinstance(data, list):
#             logging.error("Unexpected JSON structure returned")
#             return []

#         return data

#     except requests.exceptions.RequestException as e:
#         logging.error(f"HTTP request failed: {e}")
#         return []

#     except ValueError as e:
#         logging.error(f"Failed to parse JSON: {e}")
#         return []


# def display_breweries(breweries: list[dict[str, Any]]) -> None:
#     """Print brewery information in a formatted way."""

#     if not breweries:
#         logging.warning("No brewery data to display.")
#         return

#     logging.info(f"Displaying {len(breweries)} breweries...\n")

#     for brewery in breweries:
#         # Get fields with fallback if missing
#         name = brewery.get("name", "N/A")
#         website = brewery.get("website_url", "No website available")

#         print(f"Brewery Name: {name}")
#         print(f"Brewery Website: {website}\n")


# def main():
#     breweries = fetch_breweries("minneapolis")
#     display_breweries(breweries)


# if __name__ == "__main__":
#     main()


# import json

# import requests

# response = requests.get(
#     "https://api.openbrewerydb.org/v1/breweries?by_city=minneapolis"
# )
# data = json.loads(response.content)

# for o in data:
#     print(
#         f"Brewery Name: {o['name']}\nBrewery Website: {o['website_url']}\n\n"
#     )


# print(data)

# import logging
# import socket
# import time

# # --- Configuration ---
# HOST = "time.nist.gov"
# PORT = 13
# TIMEOUT = 5  # Timeout for connection and recv operations (seconds)
# MAX_RETRIES = 3  # Maximum number of connection attempts
# RETRY_DELAY = 2  # Delay between retries (seconds)

# # --- Logging Setup ---
# logging.basicConfig(
#     level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
# )
# logger = logging.getLogger(__name__)


# def get_nist_time_robust():
#     """Attempts to connect to the NIST time server and retrieve the time string."""
#     for attempt in range(1, MAX_RETRIES + 1):
#         logger.info(
#             f"Attempting to connect to {HOST}:{PORT} (Attempt {attempt}/{MAX_RETRIES})."
#         )

#         # Use 'with' statement for automatic resource management (s.close() is implicit)
#         try:
#             with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#                 # 1. Set Timeout: Prevents the program from hanging indefinitely
#                 s.settimeout(TIMEOUT)

#                 # 2. Connect and Receive Data
#                 s.connect((HOST, PORT))
#                 data = s.recv(512)

#                 # 3. Decode and Return Success
#                 time_string = data.decode().strip()
#                 logger.info("Successfully received time data.")
#                 return time_string

#         # 4. Handle Specific Errors (Transient Failures)
#         except TimeoutError:
#             logger.warning(f"Connection timed out after {TIMEOUT}s.")
#         except ConnectionRefusedError:
#             logger.warning("Connection refused by the server.")
#         except socket.gaierror:
#             logger.error(
#                 f"DNS Resolution Error: Could not resolve the hostname '{HOST}'. Aborting retries."
#             )
#             return None  # Abort because retries won't help with a permanent DNS error
#         except Exception as e:
#             logger.error(f"An unexpected error occurred: {e}")

#         # 5. Handle Retries
#         if attempt < MAX_RETRIES:
#             logger.info(f"Retrying in {RETRY_DELAY} seconds...")
#             time.sleep(RETRY_DELAY)

#     # If the loop finishes without success
#     logger.error(f"Failed to retrieve time after {MAX_RETRIES} attempts.")
#     return None


# # --- Execution ---
# if __name__ == "__main__":
#     result = get_nist_time_robust()

#     if result:
#         print("\n--- Final Result ---")
#         print(f"NIST Time: {result}")
#     else:
#         print("\n--- Final Result ---")
#         print("Operation failed.")


# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(("time.nist.gov", 13))
# data = s.recv(512)
# print(data.decode())

# s.close()

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# def validate_email(email_address):
#     # must end in .edu or .org
#     is_email = bool(
#         re.match(r"^[a-zA-Z0-9]\S*@\S+\.(org|edu)$", email_address)
#     )

#     return is_email


# if __name__ == "__main__":
#     emails = [
#         "john@stthomas.edu",
#         "anna@my-school.orgmike@gmail.com",
#         "user@123.org",
#         "bademail@org",
#     ]

#     for email in emails:
#         is_email = validate_email(email)

#         print(f"{email}: {is_email}")
