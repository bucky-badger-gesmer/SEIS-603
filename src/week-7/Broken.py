"""
Comprehensive Python Study Program
Covers: Files, Lists, Tuples, Dictionaries, Regular Expressions, and Web Services
Author: Study Guide Example
Date: 2025
"""

"""
TEST NOTES:
- Needed to import urllib.error
- Adjust append_to_file function to append instead of write
- Adjust create_person_tuple to return a tuple instead of a list
- merge_dictionaries needed to have the merged dictionary be a new dictionary, and then loop through both dict1 and dict2
- extract_phone_numbers needed the regex to be adjusted, last 4 numbers were only 3
"""


import json
import re
import urllib.error
import urllib.parse
import urllib.request

# ============================================================================
# SECTION 1: FILE OPERATIONS
# ============================================================================


def write_sample_file(filename):
    """
    Write sample data to a text file using 'with' statement.
    The 'with' automatically closes the file when done.
    """
    # Open file in write mode ('w')
    with open(filename, "w") as file_handle:
        file_handle.write("John,25,Engineer\n")
        file_handle.write("Sarah,30,Designer\n")
        file_handle.write("Mike,28,Teacher\n")
        file_handle.write("Emma,35,Doctor\n")
    print(f"File '{filename}' created successfully")


def read_file_line_by_line(filename):
    """
    Read a file line by line using 'with' statement.
    Returns a list of all lines.
    """
    lines = []
    # Open file in read mode ('r')
    with open(filename) as file_handle:
        for line in file_handle:
            # Strip removes whitespace and newline characters
            lines.append(line.strip())
    return lines


def append_to_file(filename, new_data):
    """
    Append new data to an existing file using 'a' mode.
    """
    with open(filename, "a") as file_handle:
        file_handle.write(new_data + "\n")
    print(f"Data appended to '{filename}'")


# ============================================================================
# SECTION 2: LIST OPERATIONS
# ============================================================================


def demonstrate_lists():
    """
    Demonstrates various list operations including indexing, slicing, and modification.
    """
    print("\n=== LIST OPERATIONS ===")

    # Creating a list
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    print(f"Original list: {numbers}")

    # Indexing - accessing elements by position
    print(f"First element (index 0): {numbers[0]}")
    print(f"Last element (index -1): {numbers[-1]}")
    print(f"Third element (index 2): {numbers[2]}")

    # Slicing - getting a portion of the list
    # Format: list[start:end] - gets elements from start up to (but not including) end
    print(f"First three elements [0:3]: {numbers[0:3]}")
    print(f"Elements from index 2 to 5 [2:5]: {numbers[2:5]}")
    print(f"Last three elements [-3:]: {numbers[-3:]}")
    print(f"Every other element [::2]: {numbers[::2]}")

    # Modifying lists
    numbers.append(110)  # Add element to end
    print(f"After append(110): {numbers}")

    numbers.insert(2, 25)  # Insert 25 at index 2
    print(f"After insert(2, 25): {numbers}")

    numbers.remove(30)  # Remove first occurrence of 30
    print(f"After remove(30): {numbers}")

    popped = numbers.pop()  # Remove and return last element
    print(f"Popped element: {popped}")
    print(f"After pop(): {numbers}")

    # List methods
    numbers.sort()  # Sort in ascending order
    print(f"After sort(): {numbers}")

    numbers.reverse()  # Reverse the list
    print(f"After reverse(): {numbers}")

    return numbers


def list_iteration_examples():
    """
    Shows different ways to iterate through lists.
    """
    print("\n=== LIST ITERATION ===")

    fruits = ["apple", "banana", "cherry", "date", "elderberry"]

    # Method 1: Direct iteration
    print("Method 1 - Direct iteration:")
    for fruit in fruits:
        print(f"  {fruit}")

    # Method 2: Using index with range and len
    print("\nMethod 2 - Using index:")
    for i in range(len(fruits)):
        print(f"  Index {i}: {fruits[i]}")

    # Method 3: Using enumerate to get both index and value
    print("\nMethod 3 - Using enumerate:")
    for index, fruit in enumerate(fruits):
        print(f"  Position {index}: {fruit}")


def get_list_slice(input_list, start, end):
    """
    Returns a slice of the list from start to end index.
    """
    return input_list[start : end + 1]


# ============================================================================
# SECTION 3: TUPLE OPERATIONS
# ============================================================================


def demonstrate_tuples():
    """
    Demonstrates tuple operations including creation, unpacking, and comparison.
    Tuples are immutable (cannot be changed after creation).
    """
    print("\n=== TUPLE OPERATIONS ===")

    # Creating tuples
    person1 = ("John", 25, "Engineer")
    person2 = ("Sarah", 30, "Designer")
    person3 = ("Mike", 25, "Teacher")

    print(f"Person1 tuple: {person1}")

    # Accessing tuple elements by index
    print(f"Name: {person1[0]}")
    print(f"Age: {person1[1]}")
    print(f"Job: {person1[2]}")

    # Tuple unpacking - assign each element to a variable
    name, age, job = person1
    print(f"Unpacked - Name: {name}, Age: {age}, Job: {job}")

    # Tuples can be compared
    print("\nComparing tuples:")
    print(f"person1 == person2: {person1 == person2}")
    print(
        f"person1 < person2: {person1 < person2}"
    )  # Compares element by element

    # Sorting a list of tuples
    people = [person2, person1, person3]
    print(f"\nOriginal list of tuples: {people}")

    people.sort()  # Sorts by first element, then second, etc.
    print(f"Sorted list of tuples: {people}")

    # Sort by specific element (age in this case - using beginner-friendly method)
    def get_age(person_tuple):
        return person_tuple[1]

    people.sort(key=get_age)
    print(f"Sorted by age: {people}")

    return people


def create_person_tuple(name, age, job):
    """
    Creates a person tuple from individual values.
    Returns tuple in format (name, age, job).
    """
    person = (name, age, job)
    return person


# ============================================================================
# SECTION 4: DICTIONARY OPERATIONS
# ============================================================================


def demonstrate_dictionaries():
    """
    Demonstrates dictionary operations for storing and retrieving key-value pairs.
    """
    print("\n=== DICTIONARY OPERATIONS ===")

    # Creating a dictionary
    student = {
        "name": "Alice",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
    }

    print(f"Student dictionary: {student}")

    # Accessing values by key
    print(f"\nStudent name: {student['name']}")
    print(f"Student GPA: {student['gpa']}")

    # Using get() method (safer - returns None if key doesn't exist)
    print(f"Student age: {student.get('age')}")
    print(
        f"Student minor: {student.get('minor', 'Not specified')}"
    )  # Provides default value

    # Adding new key-value pairs
    student["minor"] = "Mathematics"
    print(f"\nAfter adding minor: {student}")

    # Modifying existing values
    student["gpa"] = 3.9
    print(f"After updating GPA: {student}")

    # Removing key-value pairs
    removed_value = student.pop("minor")
    print(f"Removed minor: {removed_value}")
    print(f"After removing minor: {student}")

    # Checking if key exists
    if "name" in student:
        print("\n'name' key exists in dictionary")

    # Iterating through dictionary
    print("\nIterating through keys:")
    for key in student:
        print(f"  {key}")

    print("\nIterating through values:")
    for value in student.values():
        print(f"  {value}")

    print("\nIterating through key-value pairs:")
    for key, value in student.items():
        print(f"  {key}: {value}")

    return student


def count_words_in_file(filename):
    """
    Reads a file and counts word frequency using a dictionary.
    This is a common pattern in data processing.
    """
    word_count = {}

    with open(filename) as file_handle:
        for line in file_handle:
            # Split line into words
            words = line.strip().split(",")
            for word in words:
                # Clean up the word
                word = word.strip()
                # Count occurrences
                if word in word_count:
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1

    return word_count


def merge_dictionaries(dict1, dict2):
    """
    Merges two dictionaries. If keys overlap, dict2 values should overwrite dict1.
    Returns a new merged dictionary.
    """
    merged = {}

    for key, value in dict1.items():
        merged[key] = value

    for key, value in dict2.items():
        merged[key] = value

    return merged


# ============================================================================
# SECTION 5: REGULAR EXPRESSIONS
# ============================================================================


def demonstrate_regex_basics():
    """
    Demonstrates basic regular expression operations using the re module.
    """
    print("\n=== REGULAR EXPRESSIONS ===")

    sample_text = "Contact us at info@example.com or support@example.org. Call 555-1234 or 555-5678."

    # Finding email addresses
    print("Finding email addresses:")
    email_pattern = (
        r"\S+@\S+"  # \S+ means one or more non-whitespace characters
    )
    emails = re.findall(email_pattern, sample_text)
    for email in emails:
        print(f"  Found email: {email}")

    # Finding phone numbers
    print("\nFinding phone numbers:")
    phone_pattern = r"\d{3}-\d{4}"  # \d means digit, {3} means exactly 3 times
    phones = re.findall(phone_pattern, sample_text)
    for phone in phones:
        print(f"  Found phone: {phone}")

    # Using search to find first match
    print("\nSearching for first email:")
    match = re.search(email_pattern, sample_text)
    if match:
        print(f"  First email found: {match.group()}")
        print(f"  Position: {match.start()} to {match.end()}")

    # Replacing text
    print("\nReplacing emails:")
    censored = re.sub(email_pattern, "[EMAIL REDACTED]", sample_text)
    print(f"  {censored}")

    return emails, phones


def extract_data_with_regex(text):
    """
    Extracts structured data using regular expressions with groups.
    """
    print("\n=== EXTRACTING DATA WITH REGEX ===")

    # Pattern to extract name, age, and occupation from "Name: John, Age: 25, Job: Engineer"
    pattern = r"Name: (\w+), Age: (\d+), Job: (\w+)"

    match = re.search(pattern, text)
    if match:
        name = match.group(1)  # First group in parentheses
        age = match.group(2)  # Second group
        job = match.group(3)  # Third group

        print(f"Extracted - Name: {name}, Age: {age}, Job: {job}")
        return name, age, job
    else:
        print("No match found")
        return None, None, None


def validate_with_regex(text, pattern):
    """
    Validates if text matches a pattern (returns True/False).
    """
    # Use match() to check if pattern matches from the beginning
    if re.match(pattern, text):
        return True
    else:
        return False


def extract_phone_numbers(text):
    """
    Extracts all phone numbers in format XXX-XXX-XXXX from text.
    Returns list of phone numbers found.
    """
    pattern = r"\d{3}-\d{3}-\d{4}"
    phone_numbers = re.findall(pattern, text)
    return phone_numbers


# ============================================================================
# SECTION 6: NETWORKED PROGRAMS AND WEB SERVICES - FRUITYVICE API
# ============================================================================


def get_fruit_by_name(fruit_name):
    """
    Fetches information about a specific fruit by name from Fruityvice API.
    Returns a dictionary with fruit data.

    This demonstrates:
    - Building URLs dynamically
    - Making HTTP requests with urllib
    - Reading and decoding response data
    - Parsing JSON into Python dictionaries
    - Error handling with try/except
    """
    print(f"\n=== FETCHING INFO FOR: {fruit_name} ===")

    # Build the URL with the fruit name
    base_url = "https://www.fruityvice.com/api/fruit/"
    url = base_url + fruit_name
    print(f"Request URL: {url}")

    try:
        # Open the URL and read the response
        with urllib.request.urlopen(url) as response:
            # Read response (returns bytes)
            data_bytes = response.read()

            # Decode bytes to string (UTF-8 encoding)
            data_string = data_bytes.decode("utf-8")

            # Parse JSON string to Python dictionary
            fruit_data = json.loads(data_string)

            print(f"Successfully fetched data for {fruit_name}")
            return fruit_data

    except urllib.error.HTTPError as error:
        # Handle HTTP errors (404, 500, etc.)
        print(
            f"HTTP Error fetching fruit '{fruit_name}': {error.code} - {error.reason}"
        )
        return None
    except urllib.error.URLError as error:
        # Handle URL/network errors
        print(f"URL Error fetching fruit '{fruit_name}': {error.reason}")
        return None
    except Exception as error:
        # Handle any other errors
        print(f"Error fetching fruit '{fruit_name}': {error}")
        return None


def display_fruit_info(fruit_dict):
    """
    Displays formatted information about a fruit.
    Demonstrates accessing nested dictionary data from JSON.

    JSON structure from API:
    {
        "name": "Banana",
        "family": "Musaceae",
        "genus": "Musa",
        "order": "Zingiberales",
        "nutritions": {
            "calories": 96,
            "fat": 0.2,
            "sugar": 17.2,
            "carbohydrates": 22.0,
            "protein": 1.0
        }
    }
    """
    if fruit_dict is None:
        print("No fruit data to display")
        return

    print("\n--- Fruit Information ---")

    # Access top-level dictionary keys
    print(f"Name: {fruit_dict['name']}")
    print(f"Family: {fruit_dict['family']}")
    print(f"Genus: {fruit_dict['genus']}")
    print(f"Order: {fruit_dict['order']}")

    # Access nested dictionary - nutritions is a dictionary inside the main dictionary
    nutritions = fruit_dict["nutritions"]
    print("\nNutritional Information (per 100g):")
    print(f"  Calories: {nutritions['calories']}")
    print(f"  Fat: {nutritions['fat']}g")
    print(f"  Sugar: {nutritions['sugar']}g")
    print(f"  Carbohydrates: {nutritions['carbohydrates']}g")
    print(f"  Protein: {nutritions['protein']}g")


def compare_fruits_nutrition(fruit1_dict, fruit2_dict):
    """
    Compares nutritional values between two fruits.
    Demonstrates working with multiple dictionaries and nested data.
    """
    if fruit1_dict is None or fruit2_dict is None:
        print("Cannot compare - missing fruit data")
        return

    print(
        f"\n=== COMPARING {fruit1_dict['name'].upper()} vs {fruit2_dict['name'].upper()} ==="
    )

    # Get nutrition dictionaries from both fruits
    nutrition1 = fruit1_dict["nutritions"]
    nutrition2 = fruit2_dict["nutritions"]

    # Compare calories
    print("\nCalories:")
    print(f"  {fruit1_dict['name']}: {nutrition1['calories']}")
    print(f"  {fruit2_dict['name']}: {nutrition2['calories']}")
    if nutrition1["calories"] > nutrition2["calories"]:
        print(f"  Winner: {fruit1_dict['name']} has more calories")
    elif nutrition1["calories"] < nutrition2["calories"]:
        print(f"  Winner: {fruit2_dict['name']} has more calories")
    else:
        print("  Tie: Both have same calories")

    # Compare sugar
    print("\nSugar:")
    print(f"  {fruit1_dict['name']}: {nutrition1['sugar']}g")
    print(f"  {fruit2_dict['name']}: {nutrition2['sugar']}g")
    if nutrition1["sugar"] > nutrition2["sugar"]:
        print(f"  Winner: {fruit1_dict['name']} has more sugar")
    elif nutrition1["sugar"] < nutrition2["sugar"]:
        print(f"  Winner: {fruit2_dict['name']} has more sugar")
    else:
        print("  Tie: Both have same sugar")

    # Compare protein
    print("\nProtein:")
    print(f"  {fruit1_dict['name']}: {nutrition1['protein']}g")
    print(f"  {fruit2_dict['name']}: {nutrition2['protein']}g")
    if nutrition1["protein"] > nutrition2["protein"]:
        print(f"  Winner: {fruit1_dict['name']} has more protein")
    elif nutrition1["protein"] < nutrition2["protein"]:
        print(f"  Winner: {fruit2_dict['name']} has more protein")
    else:
        print("  Tie: Both have same protein")


def save_fruit_to_file(fruit_dict, filename):
    """
    Saves a single fruit's data to a text file.
    Demonstrates writing structured data from API to files.
    """
    if fruit_dict is None:
        print("No fruit data to save")
        return

    print(f"\n=== SAVING FRUIT TO FILE: {filename} ===")

    with open(filename, "w") as file_handle:
        file_handle.write("FRUIT INFORMATION\n")
        file_handle.write("=" * 50 + "\n\n")

        file_handle.write(f"Name: {fruit_dict['name']}\n")
        file_handle.write(f"Family: {fruit_dict['family']}\n")
        file_handle.write(f"Genus: {fruit_dict['genus']}\n")
        file_handle.write(f"Order: {fruit_dict['order']}\n\n")

        file_handle.write("Nutritional Information (per 100g):\n")
        file_handle.write("-" * 50 + "\n")

        nutritions = fruit_dict["nutritions"]
        file_handle.write(f"Calories: {nutritions['calories']}\n")
        file_handle.write(f"Fat: {nutritions['fat']}g\n")
        file_handle.write(f"Sugar: {nutritions['sugar']}g\n")
        file_handle.write(f"Carbohydrates: {nutritions['carbohydrates']}g\n")
        file_handle.write(f"Protein: {nutritions['protein']}g\n")

    print(f"Saved fruit data to {filename}")


def fetch_multiple_fruits(fruit_names_list):
    """
    Fetches data for multiple fruits and returns them in a list.
    Demonstrates looping through a list and making multiple API calls.
    """
    print("\n=== FETCHING MULTIPLE FRUITS ===")

    fruits_data = []

    for fruit_name in fruit_names_list:
        fruit_data = get_fruit_by_name(fruit_name)
        if fruit_data is not None:
            fruits_data.append(fruit_data)

    print(
        f"\nSuccessfully fetched {len(fruits_data)} out of {len(fruit_names_list)} fruits"
    )
    return fruits_data


def get_fruit_calories(fruit_name):
    """
    Gets just the calorie count for a specific fruit.
    Returns the calorie value as an integer, or None if fruit not found.
    """
    fruit_data = get_fruit_by_name(fruit_name)
    if fruit_data:
        return fruit_data["nutritions"]["calories"]
    return None


def make_api_request_with_parameters():
    """
    Demonstrates making API requests with URL parameters.
    Shows how to encode parameters for URLs.
    """
    print("\n=== API REQUEST WITH PARAMETERS ===")

    # Base URL for an example API
    base_url = "https://api.example.com/search"

    # Parameters to send with request (as a dictionary)
    parameters = {
        "query": "python programming",
        "limit": "10",
        "format": "json",
    }

    # Encode parameters for URL
    # This converts {"query": "python programming"} to "query=python+programming"
    encoded_params = urllib.parse.urlencode(parameters)
    print(f"Encoded parameters: {encoded_params}")

    # Construct full URL with parameters
    full_url = base_url + "?" + encoded_params
    print(f"Full URL: {full_url}")

    # In a real scenario, you would fetch this URL
    # For demonstration, we just show how to build it
    return full_url


# ============================================================================
# SECTION 7: INTEGRATION EXAMPLE
# ============================================================================


def process_student_data_file(input_file, output_file):
    """
    Comprehensive example that combines multiple concepts:
    - Reading from file
    - Processing with lists and dictionaries
    - Using regex for validation
    - Writing results to file
    """
    print("\n=== PROCESSING STUDENT DATA ===")

    students = []
    email_pattern = (
        r"^[\w\.-]+@[\w\.-]+\.\w+$"  # Basic email validation pattern
    )

    # Read input file
    with open(input_file) as input_handle:
        for line in input_handle:
            # Skip empty lines
            if line.strip() == "":
                continue

            # Parse line: format is "Name,Age,Email"
            parts = line.strip().split(",")

            if len(parts) == 3:
                name = parts[0].strip()
                age = parts[1].strip()
                email = parts[2].strip()

                # Validate email using regex
                if re.match(email_pattern, email):
                    # Create student dictionary
                    student = {"name": name, "age": int(age), "email": email}
                    students.append(student)
                else:
                    print(f"  Invalid email for {name}: {email}")

    print(f"Processed {len(students)} valid students")

    # Sort students by age (beginner-friendly method)
    def get_student_age(student_dict):
        return student_dict["age"]

    students.sort(key=get_student_age)

    # Write results to output file
    with open(output_file, "w") as output_handle:
        output_handle.write("Student Report\n")
        output_handle.write("=" * 50 + "\n")
        for student in students:
            output_handle.write(f"Name: {student['name']}, ")
            output_handle.write(f"Age: {student['age']}, ")
            output_handle.write(f"Email: {student['email']}\n")

    print(f"Results written to {output_file}")
    return students


# ============================================================================
# MAIN PROGRAM
# ============================================================================


def main():
    """
    Main function that demonstrates all concepts.
    """
    print("=" * 70)
    print("COMPREHENSIVE PYTHON STUDY PROGRAM")
    print("=" * 70)

    # SECTION 1: File Operations
    print("\n" + "=" * 70)
    print("SECTION 1: FILE OPERATIONS")
    print("=" * 70)
    write_sample_file("sample_data.txt")
    lines = read_file_line_by_line("sample_data.txt")
    print(f"Read {len(lines)} lines from file")
    for line in lines:
        print(f"  {line}")
    append_to_file("sample_data.txt", "Bob,32,Lawyer")

    # SECTION 2: Lists
    print("\n" + "=" * 70)
    print("SECTION 2: LIST OPERATIONS")
    print("=" * 70)
    demonstrate_lists()
    list_iteration_examples()

    # SECTION 3: Tuples
    print("\n" + "=" * 70)
    print("SECTION 3: TUPLE OPERATIONS")
    print("=" * 70)
    demonstrate_tuples()

    # SECTION 4: Dictionaries
    print("\n" + "=" * 70)
    print("SECTION 4: DICTIONARY OPERATIONS")
    print("=" * 70)
    demonstrate_dictionaries()
    word_counts = count_words_in_file("sample_data.txt")
    print("\nWord frequency in file:")
    for word, count in word_counts.items():
        print(f"  '{word}': {count}")

    # SECTION 5: Regular Expressions
    print("\n" + "=" * 70)
    print("SECTION 5: REGULAR EXPRESSIONS")
    print("=" * 70)
    demonstrate_regex_basics()
    sample = "Name: Alice, Age: 22, Job: Developer"
    extract_data_with_regex(sample)

    # Test email validation
    test_email = "user@example.com"
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    is_valid = validate_with_regex(test_email, email_pattern)
    print(f"\nValidating '{test_email}': {is_valid}")

    # SECTION 6: Web Services - FRUITYVICE API
    print("\n" + "=" * 70)
    print("SECTION 6: WEB SERVICES - FRUITYVICE API")
    print("=" * 70)

    # Fetch individual fruits by name
    banana_data = get_fruit_by_name("banana")
    if banana_data:
        display_fruit_info(banana_data)
        save_fruit_to_file(banana_data, "banana_data.txt")

    apple_data = get_fruit_by_name("apple")
    if apple_data:
        display_fruit_info(apple_data)

    # Compare two fruits
    if banana_data and apple_data:
        compare_fruits_nutrition(banana_data, apple_data)

    # Fetch multiple fruits at once
    fruit_names = ["strawberry", "mango", "orange"]
    multiple_fruits = fetch_multiple_fruits(fruit_names)

    print("\nDisplaying all fetched fruits:")
    for fruit in multiple_fruits:
        print(
            f"  - {fruit['name']}: {fruit['nutritions']['calories']} calories"
        )

    # Show how to build URLs with parameters
    make_api_request_with_parameters()

    # SECTION 7: Integration Example
    print("\n" + "=" * 70)
    print("SECTION 7: INTEGRATION EXAMPLE")
    print("=" * 70)

    # Create sample input file with student data
    with open("students_input.txt", "w") as f:
        f.write("Alice Johnson,20,alice@example.com\n")
        f.write("Bob Smith,22,bob@example.com\n")
        f.write("Charlie Brown,19,charlie.invalid\n")  # Invalid email
        f.write("Diana Prince,21,diana@example.org\n")

    process_student_data_file("students_input.txt", "students_output.txt")

    # Show final output
    print("\nFinal output file contents:")
    with open("students_output.txt") as f:
        for line in f:
            print(f"  {line}", end="")

    print("\n\n" + "=" * 70)
    print("PROGRAM COMPLETE")
    print("=" * 70)


# Run the main program
if __name__ == "__main__":
    main()
