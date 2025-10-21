import re
import socket
import urllib.request


def exercise_1():
    url_input = input("Enter a url: ")

    url_input_strip = url_input.strip()
    try:
        validate_url(url_input_strip)
    except ValueError:
        print(
            f"Invalid URL: {url_input_strip}; enter a valid url, like http://data.pr4e.org/romeo.txt"
        )
        exit()

    host_from_input = url_input_strip.split("/")[2]

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host_from_input, 80))

    request_str = f"GET {url_input_strip} HTTP/1.0\r\n\r\n"
    mysocket.send(request_str.encode())

    data = mysocket.recv(512)

    while len(data) > 1:
        print(data.decode())
        data = mysocket.recv(512)

    mysocket.close()


def exercise_2():
    url_input = input("Enter a url: ")

    url_input_strip = url_input.strip()
    try:
        validate_url(url_input_strip)
    except ValueError:
        print(
            f"Invalid URL: {url_input_strip}; enter a valid url, like http://data.pr4e.org/mbox-short.txt"
        )
        exit()

    host_from_input = url_input_strip.split("/")[2]

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host_from_input, 80))

    request_str = f"GET {url_input_strip} HTTP/1.0\r\n\r\n"
    mysocket.send(request_str.encode())

    data = mysocket.recv(512)
    data_doc = ""

    while len(data) > 1:
        data_doc += data.decode()
        data = mysocket.recv(512)

    data_doc_first_3000 = ""
    count = 0

    # it's entirely possible that the doc could be less than 3000 characters!
    for char in data_doc:
        if re.match(r"\S", char):
            count += 1
        data_doc_first_3000 += char
        if count >= 3000:
            break

    print(data_doc_first_3000)
    print("\n======== RESULTS ========")
    print(f"Total number of characters in document: {len(data_doc)}\n")

    mysocket.close()


def exercise_3():
    url_input = input("Enter a url: ")
    url_input_strip = url_input.strip()

    try:
        fh = urllib.request.urlopen(url_input_strip)
    except ValueError:
        print(
            f"Invalid URL: {url_input_strip}; enter a valid url, like http://data.pr4e.org/mbox-short.txt"
        )
        exit()

    first_3000_chars = ""
    total_non_whitespace = 0

    for line in fh:
        decoded_line = line.decode()
        total_non_whitespace += len(re.findall(r"\S", decoded_line))

        if len(first_3000_chars) < 3000:
            needed = 3000 - len(first_3000_chars)
            first_3000_chars += decoded_line[:needed]

    print(first_3000_chars)
    print("\n======== RESULTS ========")
    print(
        f"\nTotal number of non-whitespace characters in document: {total_non_whitespace}"
    )


def validate_url(url_str):
    is_valid = bool(
        re.match(
            r"^https?:\/\/(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,63}(?:\/.*)?$",
            url_str,
        )
    )

    if not is_valid:
        raise ValueError()


if __name__ == "__main__":
    # exercise_1()
    exercise_2()
    # exercise_3()
