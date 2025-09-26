from inclass import count_vowels, is_palindrome, reverse_words


def test_count_vowels_basic():
    assert count_vowels("banana") == 3
    assert count_vowels("apple") == 2
    assert count_vowels("aeiou") == 5
    assert count_vowels("cysts") == 0
    assert count_vowels(None) == 0


def test_count_vowels_empty():
    assert count_vowels(None) == 0
    assert count_vowels("") == 0
    assert count_vowels("    ") == 0
    assert count_vowels("123") == 0
    assert count_vowels(1) == 0


def test_count_vowels_uppercase():
    assert count_vowels("BANANA") == 3
    assert count_vowels("APPLE") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("CYSTS") == 0
    assert count_vowels("bAnaNa") == 3


def test_reverse_words_basic():
    assert reverse_words("Hello World") == "World Hello"
    assert (
        reverse_words("Hello world from Python") == "Python from world Hello"
    )
    assert reverse_words(None) is None
    assert reverse_words("") == ""
    assert reverse_words("    ") == ""


def test_reverse_words_single_word():
    assert reverse_words("BANANA") == "BANANA"
    assert reverse_words("apple") == "apple"
    assert reverse_words("aEiOu") == "aEiOu"
    assert reverse_words(123) is None


def test_reverse_words_spaces():
    assert reverse_words("Hello    World    ") == "World Hello"
    assert reverse_words("Hello    World") == "World Hello"
    assert reverse_words("Hello        World        ") == "World Hello"


def test_is_palindrome_basic():
    assert is_palindrome("racecar") is True
    assert is_palindrome("A") is True
    assert is_palindrome("    A    ") is True
    assert is_palindrome("12321") is True
    assert is_palindrome("") is True
    assert is_palindrome("    ") is True


def test_is_palindrome_mixed_case():
    assert is_palindrome("rAcECaR") is True
    assert is_palindrome(" RACEcar ") is True
    assert is_palindrome("Never odd or even") is True
    assert is_palindrome("NEVER ODD OR EVEN") is True
    assert is_palindrome("NEVER    ODD    OR    even    ") is True


def test_is_palindrome_false_case():
    assert is_palindrome("12") is False
    assert is_palindrome("    ABC    ") is False
    assert is_palindrome(1) is False
    assert is_palindrome(None) is False
