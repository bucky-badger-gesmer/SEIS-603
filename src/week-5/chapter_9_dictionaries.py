name = input("Enter file: ")

try:
    fh = open(name)
except:
    print("File not found: ", name)
    exit()

# Look for From lines and take second word who sent the mail
# create a dictionary to map email and number of times they appear in the file

email_dictionary = dict()

for line in fh:
    if "From " not in line:
        continue

    start_index = line.find("From ") + len("From ")
    email = line[start_index:].split()[0]
    email_dictionary[email] = email_dictionary.get(email, 0) + 1

# print(email_dictionary)

value_list = list(email_dictionary.values())
highest_value = max(value_list)

# loop through dictionaries and find the entry with the hight_value
for email_key in email_dictionary:
    if email_dictionary[email_key] == highest_value:
        print(f"{email_key} {email_dictionary[email_key]}")


stuff = dict()
print(stuff.get("candy", "poopy poop"))
