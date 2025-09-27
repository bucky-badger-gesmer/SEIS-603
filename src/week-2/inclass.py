def count_vowels(s):
    vowels = "aeiou"
    count = 0

    try:
        for c in s:
            if c.lower() in vowels:
                count += 1

        return count
    except TypeError:
        print("Invalid value passed to count_vowels")
        return 0


def reverse_words(s):
    words_reverse = ""

    try:
        words = s.split()

        for i in range(len(words) - 1, -1, -1):
            words_reverse = words_reverse + words[i] + " "

        words_reverse_result = words_reverse.strip()

        return words_reverse_result
    except AttributeError:
        print("Invalid value passed to reverse_words")
        return None


def is_palindrome(s):
    try:
        s_formatted = "".join(s.split())

        for forward_index in range(len(s_formatted)):
            backward_index = len(s_formatted) - forward_index - 1

            if forward_index >= backward_index:
                break

            if (
                s_formatted[forward_index].lower()
                != s_formatted[backward_index].lower()
            ):
                return False

        return True
    except AttributeError:
        print("Invalid non-string value passed to is_palindrome")
        return False


if __name__ == "__main__":
    while True:
        print("\n\n======== Welcome! ========")
        user_input = input("Enter a text string, or 'q' to quit: ")

        if user_input == "q":
            break
        elif user_input.strip() == "":
            print("Please enter a valid input.")

        vowels = count_vowels(user_input)
        user_input_reverse = reverse_words(user_input)
        is_user_input_palindrome = is_palindrome(user_input)

        print("\n\n======== RESULTS ========")
        print("Text provided:", user_input)
        print("\nVowel count:", vowels)
        print("Words in reverse order:", user_input_reverse)
        print("Is it a palindrome:", is_user_input_palindrome)

    print("\nQuitting program...")
    print("Goodbye!\n")
