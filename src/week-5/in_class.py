import string


def practice_function_1():
    student_scores = {}

    student_scores["Alex"] = 85
    student_scores["Aaron"] = 92
    student_scores["Michael"] = 100

    for key in student_scores:
        print(f"{key}, {student_scores[key]}")


def practice_function_2():
    pets = {"dog": 2, "cat": 4}
    pet_type_input = input("Enter a pet type: ")
    pet_value_input = input("Enter the pet value: ")

    try:
        pet_value = int(pet_value_input)
        pets[pet_type_input] = pets.get(pet_type_input, 0) + pet_value
    except ValueError:
        print("Invalid pet value entered")

    print(pets)


def practice_function_3():
    name_counts = {}
    names = ["csev", "cwen", "csev", "zqian", "cwen", "zqian", "zqian"]

    for name in names:
        name_counts[name] = name_counts.get(name, 0) + 1

    print(name_counts)


def practice_function_4():
    word_counts = {}

    line_of_text_input = input("Enter a line of text: ")
    words = line_of_text_input.split()

    for word in words:
        word_transform = word.translate(
            word.maketrans("", "", string.punctuation)
        )
        word_counts[word_transform.lower()] = (
            word_counts.get(word_transform.lower(), 0) + 1
        )

    print(word_counts)


def practice_big_count_function():
    name = input("Enter file: ")
    handle = open(name, encoding="utf-8")
    text = handle.read()
    words = text.split()

    counts = dict()
    for word in words:
        word_transform = word.translate(
            word.maketrans("", "", string.punctuation)
        )
        counts[word_transform.lower()] = (
            counts.get(word_transform.lower(), 0) + 1
        )

    count_items = counts.items()
    print(counts)

    print(len(count_items))

    # file_name = input("Enter a file name: ")

    # try:
    #     fh = open(file_name)
    # except FileNotFoundError:
    #     print("file not found!")
    #     exit()

    # word_counts = {}

    # for line in fh:
    #     line_strip = line.strip()

    #     for word in line_strip:
    #         print("word: ", word)

    # print(word_counts)


# practice_function_1()
# practice_function_2()
# practice_function_3()
# practice_function_4()
practice_big_count_function()
