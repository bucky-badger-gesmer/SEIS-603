fh = open("mbox.txt")

domains = []

for line in fh:
    line_rstrip = line.rstrip()

    # PART 1:
    # print(line_rstrip)

    if "Received: from" in line_rstrip:
        # PART 2:
        first_split = line_rstrip.split("Received: from ")
        domain_split = first_split[1].split()

        domain = domain_split[0]

        # PART 3:
        if domain not in domains:
            domains.append(domain)

print("DOMAINS: ", domains)
fh.close()
