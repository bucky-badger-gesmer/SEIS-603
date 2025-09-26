from inclass import count_vowels, is_palindrome, reverse_words


def test_count_vowels():
    assert count_vowels("banana") == 3
    assert count_vowels("apple") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("cysts") == 0
    assert count_vowels(1) == 0


def test_reverse_Words():
    assert reverse_words("Hello World") == "World Hello"


def test_is_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True
    assert is_palindrome(None) == False
