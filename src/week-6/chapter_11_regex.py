import re

fh = open("regex_sum_2291555.txt")

number_sum = 0

for line in fh:
    line_rstrip = line.rstrip()

    # foo = re.findall(r"[0-9]+", line_rstrip)
    if re.search(r"[0-9]+", line_rstrip):
        numbers_in_line = re.findall(r"[0-9]+", line_rstrip)
        print("numbers_in_line", numbers_in_line)

        for num in numbers_in_line:
            num_int = int(num)
            number_sum += num_int

print("number_sum", number_sum)


x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)
