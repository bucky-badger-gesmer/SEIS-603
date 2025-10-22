import xmlschema

my_schema = xmlschema.XMLSchema("vehicle.xsd")

print(my_schema.is_valid("vehicles.xml"))
print(my_schema.is_valid("bad.xml"))
