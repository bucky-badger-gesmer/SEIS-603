fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    exit()

counts = dict()

for line in fhand:
    words = line.split()

    for word in words:
        counts[word] = counts.get(word, 0) + 1

key_list = list(counts.keys())
print(key_list)
key_list.sort()
print(key_list)

# print(counts)
