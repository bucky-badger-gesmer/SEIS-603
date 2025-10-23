"""
Pytest Test Suite for Python Study Program
One test per section to identify bugs in the code
Run with: pytest test_study_program.py -v
"""

from Broken import (
    append_to_file,
    create_person_tuple,
    extract_phone_numbers,
    get_list_slice,
    merge_dictionaries,
    process_student_data_file,
    read_file_line_by_line,
)

# ============================================================================
# SECTION 1: FILE OPERATIONS TEST
# ============================================================================


def test_append_to_file_preserves_existing_content(tmp_path):
    """
    Test that append_to_file actually appends and doesn't overwrite.

    Creates a file with 2 lines, then appends a 3rd line.
    The file should have all 3 lines after appending.
    """
    test_file = tmp_path / "test_append.txt"

    # Create initial file with content
    with open(test_file, "w") as f:
        f.write("Line 1\n")
        f.write("Line 2\n")

    # Append new content
    append_to_file(str(test_file), "Line 3")

    # Read all lines
    lines = read_file_line_by_line(str(test_file))

    # Should have 3 lines total, not just 1
    assert len(lines) == 3, (
        f"Expected 3 lines after append, but got {len(lines)}"
    )
    assert lines[0] == "Line 1"
    assert lines[1] == "Line 2"
    assert lines[2] == "Line 3"


# ============================================================================
# SECTION 2: LIST OPERATIONS TEST
# ============================================================================


def test_get_list_slice_returns_correct_elements():
    """
    Test that list slicing returns the correct number of elements.

    Standard Python slicing [1:3] returns elements at index 1 and 2 (not including 3).
    get_list_slice(list, 1, 3) should return elements from index 1 to 3 inclusive.
    """
    test_list = [10, 20, 30, 40, 50]

    # Get slice from index 1 to 3
    result = get_list_slice(test_list, 1, 3)

    # Should return [20, 30, 40] - three elements at indices 1, 2, 3
    expected = [20, 30, 40]
    assert result == expected, f"Expected {expected}, but got {result}"


# ============================================================================
# SECTION 3: TUPLE OPERATIONS TEST
# ============================================================================


def test_create_person_tuple_returns_tuple_type():
    """
    Test that create_person_tuple returns an actual tuple, not a list.

    Tuples are immutable and can be compared/sorted differently than lists.
    The function should return a tuple like ("Alice", 25, "Engineer").
    """
    result = create_person_tuple("Alice", 25, "Engineer")

    # Must be a tuple type
    assert isinstance(result, tuple), (
        f"Expected tuple, but got {type(result).__name__}"
    )

    # Should have correct values
    assert result[0] == "Alice"
    assert result[1] == 25
    assert result[2] == "Engineer"


# ============================================================================
# SECTION 4: DICTIONARY OPERATIONS TEST
# ============================================================================


def test_merge_dictionaries_does_not_modify_original():
    """
    Test that merge_dictionaries creates a new dict without modifying the originals.

    When merging two dictionaries, the original dictionaries should remain unchanged.
    Only the returned dictionary should contain the merged data.
    """
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}

    # Store original values
    dict1_original = dict1.copy()

    # Merge dictionaries
    result = merge_dictionaries(dict1, dict2)

    # Result should have all keys
    assert "a" in result and result["a"] == 1
    assert "b" in result and result["b"] == 2
    assert "c" in result and result["c"] == 3
    assert "d" in result and result["d"] == 4

    # Original dict1 should NOT be modified
    assert dict1 == dict1_original, (
        "dict1 was modified! Should create new dictionary instead."
    )


# ============================================================================
# SECTION 5: REGULAR EXPRESSIONS TEST
# ============================================================================


def test_extract_phone_numbers_correct_format():
    """
    Test that phone numbers are extracted in the correct XXX-XXX-XXXX format.

    Phone numbers should have format: 3 digits - 3 digits - 4 digits
    Example: 555-123-4567
    """
    text = "Call me at 555-123-4567 or text 555-987-6543 anytime"

    result = extract_phone_numbers(text)

    # Should find both phone numbers
    assert len(result) == 2, (
        f"Expected 2 phone numbers, but found {len(result)}: {result}"
    )
    assert "555-123-4567" in result, (
        f"Should find 555-123-4567, but got {result}"
    )
    assert "555-987-6543" in result, (
        f"Should find 555-987-6543, but got {result}"
    )


# ============================================================================
# SECTION 7: INTEGRATION TEST
# ============================================================================


def test_process_student_data_sorts_by_age(tmp_path):
    """
    Test that student data is processed correctly and sorted by age.

    The function should:
    1. Read student data from file
    2. Validate email addresses
    3. Sort students by age (youngest first)
    4. Write results to output file
    """
    input_file = tmp_path / "test_students.txt"
    output_file = tmp_path / "test_output.txt"

    # Create test input file with students in random age order
    with open(input_file, "w") as f:
        f.write("Alice,25,alice@example.com\n")
        f.write("Bob,22,bob@test.org\n")
        f.write(
            "Charlie,19,charlie.invalid\n"
        )  # Invalid email - should be skipped
        f.write("Diana,24,diana@school.edu\n")

    # Process the file
    result = process_student_data_file(str(input_file), str(output_file))

    # Should return 3 valid students (Charlie's email is invalid)
    assert len(result) == 3, (
        f"Expected 3 valid students (Charlie has invalid email), got {len(result)}"
    )

    # Check students are sorted by age (youngest to oldest)
    assert result[0]["name"] == "Bob" and result[0]["age"] == 22, (
        "First should be Bob (age 22)"
    )
    assert result[1]["name"] == "Diana" and result[1]["age"] == 24, (
        "Second should be Diana (age 24)"
    )
    assert result[2]["name"] == "Alice" and result[2]["age"] == 25, (
        "Third should be Alice (age 25)"
    )

    # Output file should exist
    assert output_file.exists(), "Output file should be created"
