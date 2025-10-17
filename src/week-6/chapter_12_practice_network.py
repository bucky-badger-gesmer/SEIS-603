import re
import socket


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
    print("host_from_input", host_from_input)

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
    print("host_from_input", host_from_input)

    mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysocket.connect((host_from_input, 80))

    request_str = f"GET {url_input_strip} HTTP/1.0\r\n\r\n"
    mysocket.send(request_str.encode())

    data = mysocket.recv(512)

    while len(data) > 1:
        print("starting...")
        data_decoded = data.decode()
        data_decoded_split = data_decoded.split("\n")
        print("poop", data_decoded_split)

        # print(data.decode())
        print("ending...")
        data = mysocket.recv(512)

    mysocket.close()


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
