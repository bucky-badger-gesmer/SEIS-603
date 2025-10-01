# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

line_count_total = 0
line_count = 0

# print("poop", len(fh))

for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        line_value = line.split(":")[1]
        line_value_float = float(line_value)

        line_count_total += line_value_float
        line_count += 1

line_count_average = line_count_total / line_count

print("Average spam confidence:", line_count_average)
