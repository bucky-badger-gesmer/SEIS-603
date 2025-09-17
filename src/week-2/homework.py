
def sum_of_list(nums):
    current_sum = 0

    for num in nums:
        is_num_valid = is_valid_number(num)

        if not is_num_valid:
            continue

        current_sum += float(num)
    return current_sum

def find_smallest(nums):
    smallest = None

    for num in nums:
        is_num_valid = is_valid_number(num)

        if not is_num_valid:
            continue

        num_format = float(num)
        
        if smallest is None or num_format < smallest:
            smallest = num_format

    return smallest

def extract_domain(email):
    if "@" not in email or email.count("@") > 1 or " " in email.strip():
        print("Invalid email address. Please enter a valid email address.")
        return None

    domain_begin_index = email.find("@")

    domain = email[domain_begin_index + 1:]

    if len(domain) == 0:
        return None

    return domain

def is_valid_number(s):
    try:
        if s is None:
            return False

        float(s)
        return True
    except ValueError:
        return False

def prompt_user_for_numbers():
    nums = []
    while True:
        my_input = input("Enter a number or press 'Enter' to finish: ")
        if my_input.strip() == "":
            if len(nums) == 0:
                print("No numbers entered. Please enter at least one number.")
                continue
            break
        
        is_valid = is_valid_number(my_input)
        if is_valid is False:
            print("Please enter a valid number.")
            continue
        nums.append(float(my_input))

    return nums

def prompt_user_for_email():
    while True:
        email_input = input("Enter an email address: ")
        if "@" not in email_input or email_input.count("@") > 1:
            print("Invalid email address. Please enter a valid email address.")
            continue
        elif " " in email_input.strip():
            print("Invalid email address. Do not enter spaces in the email address.")
            continue

        return email_input


if __name__ == "__main__":
    while True:
        print("\n\n======== BEGIN PROGRAM ========")
        begin_input = input("Enter any key to begin the program, or 'q' to quit: ")

        if begin_input.strip() == "q":
            break

        print("\n\n======== ENTER NUMBERS ========")
        nums = prompt_user_for_numbers()


        print("\n\n======== ENTER AN EMAIL ADDRESS ========")
        email_input = prompt_user_for_email()

        print("\n\n======== RESULTS ========")
        print("nums:", nums)
        
        sum_of_nums = sum_of_list(nums)
        print("sum of nums:", round(sum_of_nums, 2))

        smallest_num = find_smallest(nums)
        print("smallest num:", smallest_num)

        print("email:", email_input)
        domain = extract_domain(email_input)
        print("domain:", domain)

    print("\n\nQuitting program...")
    print("Goodbye!\n\n")
 