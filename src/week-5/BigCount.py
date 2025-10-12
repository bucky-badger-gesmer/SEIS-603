import string

name = input("Enter file: ")
handle = open(name, encoding="utf-8")
text = handle.read()
words = text.split()

counts = dict()
for word in words:
    word_transform = word.translate(word.maketrans("", "", string.punctuation))
    counts[word_transform.lower()] = counts.get(word_transform.lower(), 0) + 1

count_items = counts.items()
print(len(count_items))

lst = []

for key, val in counts.items():
    lst.append((val, key))

lst = sorted(lst, reverse=True)
for val, key in lst[:10]:
    print(key, val)


# bigcount = None

# bigword = None
# for word, count in counts.items():
#     if bigcount is None or count > bigcount:
#         bigword = word
#         bigcount = count

# print(bigword, bigcount)
