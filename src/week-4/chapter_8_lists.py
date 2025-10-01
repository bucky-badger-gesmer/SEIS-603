# fname = input("Enter file name: ")
# fh = open(fname)

# lst = list()

# for line in fh:
#     file_line = line.rstrip()

#     words = line.rstrip().split()

#     for word in words:
#         if word not in lst:
#             lst.append(word)

# lst.sort()
# print("result", lst)


fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        email_address = line.split()[1]
        print(email_address)
        count += 1


print("There were", count, "lines in the file with From as the first word")
