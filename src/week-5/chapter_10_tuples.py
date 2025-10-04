file_name = input("Enter file name: ")

try:
    fh = open(file_name)
except FileNotFoundError:
    print("File not found. Enter a valid file name.")
    exit()

hours = {}

for line in fh:
    if "From " not in line:
        continue

    line_split = line.split(":")
    time_split = line_split[0].split()
    hour = time_split[len(time_split) - 1]

    hours[hour] = hours.get(hour, 0) + 1


# print(hours)

hours_list = list(hours.items())
hours_list.sort()


for key, value in hours_list:
    print(key, value)


# txt = "but soft what light in yonder window breaks"
# words = txt.split()

# t = list()

# for word in words:
#     t.append((len(word), word))
# print("t", t)

# t.sort(reverse=True)
# res = list()

# for length, word in t:
#     res.append(word)

# print(res)
