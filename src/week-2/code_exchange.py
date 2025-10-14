# Count vowels
def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s.lower() if char in vowels)


# Reverse strings
def reverse_words(s):
    words = s.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


# Returns True if the string is the same forwards and backwards (ignoring spaces and case), otherwise False.


def is_palindrome(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


def main():
    user_input = input("Enter a string: ")
    num_vowels = count_vowels(user_input)
    reversed_str = reverse_words(user_input)
    palindrome = is_palindrome(user_input)

    print(f"Number of vowels: {num_vowels}")
    print(f"Words in reverse order: {reversed_str}")
    print(f"Is palindrome: {palindrome}")


if __name__ == "__main__":
    main()
