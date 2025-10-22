import xml.etree.ElementTree as ET

data0 = """
<person>
<name>Chuck</name>
<phone type="intl">
  +1 734 303 4456
</phone>
<email hide="yes" />
</person>"""

my_file = open("person.xml")
data = my_file.read()

tree = ET.fromstring(data)
print("Name:", tree.find("name").text)
print("Phone:", tree.find("phone").text.strip())
print("Type?", tree.find("phone").get("type"))
print("Attr:", tree.find("email").get("hide"))
