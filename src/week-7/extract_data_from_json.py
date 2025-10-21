import json
import urllib.request

url = input("Enter location: ")
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_42.json"

print("Retrieving", url)

uh = urllib.request.urlopen(url)
data = uh.read().decode()
data_json = json.loads(data)

comments = data_json["comments"]
count_lst = []

for comment in comments:
    # print("comment obj:", comment)
    count_lst.append(int(comment["count"]))

print("Count:", len(count_lst))
print("Sum:", sum(count_lst))


# foo = [ "Glenn", "Sally", "Jen" ]
bar = json.loads('[ "Glenn", "Sally", "Jen" ]')

print("bar", bar)

# data = """
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]"""

# info = json.loads(data)
# print("User count:", len(info))

# for item in info:
#     print("Name", item["name"])
#     print("Id", item["id"])
#     print("Attribute", item["x"])
