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
        return 0


def reverse_words(s):
    print("original string: ", s)
    words_reverse = ""

    try:
        words = s.split()

        for i in range(len(words) - 1, -1, -1):
            words_reverse = words_reverse + words[i] + " "

        return words_reverse.strip()
    except AttributeError:
        print("Invalid value passed to reverse_words")
        return None


def is_palindrome(s):
    try:
        for forward_index in range(len(s)):
            backward_index = len(s) - forward_index - 1

            if forward_index == backward_index:
                break

            if s[forward_index].lower() != s[backward_index].lower():
                return False

        return True
    except TypeError:
        print("Invalid value passed to is_palindrome")
        return False


if __name__ == "__main__":
    pass
    # vowel_count = count_vowels(12.3333)
    # print("vowel_count: ", vowel_count)

    # reverse_words(12)

    # foo = is_palindrom(1)
    # print("foo: ", foo)
