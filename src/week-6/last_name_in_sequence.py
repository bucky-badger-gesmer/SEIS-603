import ssl  # defauts to certicate verification and most secure protocol (now TLS)
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL: ")
count_input = input("Enter count: ")
position_input = input("Enter position: ")


for i in range(1, int(count_input) + 2):
    print("Retrieving:", i, url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    links = soup("a")
    link = links[int(position_input) - 1]

    url = link.get("href", None)
