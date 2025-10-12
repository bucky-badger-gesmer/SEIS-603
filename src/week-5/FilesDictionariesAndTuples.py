"""
------------------------------------------------------------
SEIS-603 Foundations of Python
Homework Assignment: FilesDictionariesAndTuples

Name: Aaron Gesmer
Date: 10/12/2025

Description:
    Given a book from Project Gutenberg, use a combination
    of file handling, dictionaries, and tuples to return the
    top 10 most popular words, top 10 least popular words,
    and the number of unique words that appear in said book.

    This program was originally developed using the book
    "The Odyssey" by Homer (saved as "the-odyssey.txt"):
    https://gutenberg.org/cache/epub/1727/pg1727.txt
------------------------------------------------------------
"""

import string


def read_file():
    file_name = input("Enter a file name: ")

    try:
        fh = open(file_name, encoding="UTF-8", errors="replace")
    except FileNotFoundError:
        print("That file was not found. Exiting program.")
        exit()

    return fh


def get_word_count_dict(fh):
    word_count_dict = {}

    for line in fh:
        if line.strip() == "":
            continue

        words = line.split()

        for word in words:
            word_transform = word.translate(
                word.maketrans("", "", string.punctuation)
            )

            if word_transform.strip() == "":
                continue

            word_transform_lower = word_transform.lower()
            word_count_dict[word_transform_lower] = (
                word_count_dict.get(word_transform_lower, 0) + 1
            )

    return word_count_dict


def get_word_info(word_count_dict):
    word_count_sorted = sorted(
        [(value, key) for key, value in word_count_dict.items()]
    )
    word_count_sorted_reversed = sorted(
        [(value, key) for key, value in word_count_dict.items()], reverse=True
    )

    top_ten_words = word_count_sorted_reversed[0:10]
    least_ten_words = word_count_sorted[0:10]

    most_popular_words = [(value) for _, value in top_ten_words]
    least_popular_words = [(value) for _, value in least_ten_words]

    return (most_popular_words), (least_popular_words), (len(word_count_dict))


if __name__ == "__main__":
    fh = read_file()
    word_count_dict = get_word_count_dict(fh)
    ten_most_popular_words, ten_least_popular_words, number_of_unique_words = (
        get_word_info(word_count_dict)
    )

    print("\n======== RESULTS ========")
    print("10 Most Popular Words (Descending Order):", ten_most_popular_words)
    print("10 Least Popular Words (Ascending Order):", ten_least_popular_words)
    print("Number of Unique Words:", number_of_unique_words)
    print("\n")
