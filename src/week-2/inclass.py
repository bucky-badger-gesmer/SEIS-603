def count_vowels(s):
    vowels = "aeiou"
    count = 0

    try:
        for c in s:
            if c in vowels:
                count += 1

        return count
    except TypeError:
        print("Invalid value passed to count_vowels")
        return None


def reverse_words(s):
    print("original string: ", s)
    words_reverse = ""

    try:
        words = s.split()

        for i in range(len(words) - 1, -1, -1):
            words_reverse = words_reverse + words[i] + " "

        return words_reverse
    except AttributeError:
        print("Invalid value passed to reverse_words")
        return None


# def is_palindrom(s):
#     print("original string: ", s)

#     for i in range(len(s)):
#         for j in range(len(s) - 1, -1, -1):
#             print("i", s[i])
#             print("j", s[j])
#             if i == j:
#                 break
#             if s[i] != s[j]:
#                 return False
#     return True


if __name__ == "__main__":
    # vowel_count = count_vowels(12.3333)
    # print("vowel_count: ", vowel_count)

    # reverse_words(12)

    foo = is_palindrom("racecar")
    print("foo: ", foo)
