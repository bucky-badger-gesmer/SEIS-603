from homework import extract_domain, find_smallest, sum_of_list


def test_sum_of_list():
    assert sum_of_list([1, 2, 3]) == 6
    assert sum_of_list([1, "2", 3]) == 6
    assert sum_of_list([1, None, "foo", 2]) == 3
    assert sum_of_list([None, "None", 1, 1.000001]) == 2.000001
    assert sum_of_list([1, 2.5, 3]) == 6.5
    assert sum_of_list([]) == 0
    assert sum_of_list([None, "foo", "bar"]) == 0
    assert sum_of_list([-1, -2.5, -3]) == -6.5


def test_find_smallest():
    assert find_smallest([1, 2, 3]) == 1
    assert find_smallest([6, 12, 45, -1, 100, -100]) == -100
    assert find_smallest([1, -100.5, 20, 33]) == -100.5
    assert find_smallest(["-100", 1, 2, 3]) == -100
    assert find_smallest(["1", None, "10.5", "foo", -70.5, "-89.1"]) == -89.1
    assert find_smallest([]) is None
    assert find_smallest([None, "foo", "bar"]) is None
    assert find_smallest([42]) == 42
    assert find_smallest(["-10", "20", "0"]) == -10


def test_extract_domain():
    assert extract_domain("aaron@test.com") == "test.com"
    assert extract_domain("aaron") is None
    assert extract_domain("test@test.com.foo.bar") == "test.com.foo.bar"
    assert extract_domain("    aaron@ a.com") is None
    assert extract_domain("test@domain@domain@domain.com") is None
    assert extract_domain("") is None
    assert extract_domain("   ") is None
    assert extract_domain("USER@DOMAIN.COM") == "DOMAIN.COM"
    assert extract_domain("name@") is None
