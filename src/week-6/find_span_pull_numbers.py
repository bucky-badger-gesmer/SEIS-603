import ssl  # defauts to certicate verification and most secure protocol (now
import urllib.error
import urllib.parse
import urllib.request

from bs4 import BeautifulSoup

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter - ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

sum = 0

# Retrieve all of the span tags
tags = soup("span")
for tag in tags:
    # print(tag.contents[0])
    sum += int(tag.contents[0])

print("sum:", sum)
