fh = open("gitlog.txt")

authors = []

for line in fh:
    line_format = line.strip()

    start = line_format.find("Author:") + len("Author:")
    end = line_format.find("<")

    if "Author: " in line_format:
        author = line_format[start:end].strip()

        if author not in authors:
            authors.append(author)

authors.sort()

for author in authors:
    print(author)

fh.close()
