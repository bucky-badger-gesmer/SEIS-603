def chapter_1():
    print("Aaron Gesmer")
    for i in range(0, 4):
        print(i)


def calc_average(num1, num2):
    average = (num1 + num2) / 2
    return average


def chapter_2():
    average = calc_average(23, 34)
    print("Average:", average)


def chapter_3():
    age_input = input("Enter age: ")

    try:
        age = int(age_input)

        if age < 13 and age > 0:
            print("Child")
        elif age >= 13 and age <= 19:
            print("Teen")
        elif age >= 20:
            print("Adult")
        else:
            print("That is not a reasonable age.")
    except:
        print("Please enter a valid age.")


def exponentiate_number(num, power):
    try:
        n = float(num)

        return n**power
    except:
        return None


def chapter_4():
    a = exponentiate_number(5, 2)
    b = exponentiate_number(3, 3)

    print("a:", a)
    print("b:", b)


def chapter_5():
    sum = 0
    count = 0

    while True:
        # keep asking for a number, if there's an error, keep asking until you hit 5 entered:

        if count == 5:
            break

        num_input = input("Enter a number: ")
        try:
            num = float(num_input)

            sum = sum + num
            count = count + 1
        except:
            print("Invalid number; please enter a valid number")

    print("the sum of the numbers entered is:", sum)


def chapter_6():
    name_input = input("Enter your full name, first and last: ")

    name_lower = name_input.lower()
    print("Name in lower case:", name_lower)

    num_of_characters = len(name_lower)
    print("Number of characters in name:", num_of_characters)

    first_name_index = name_input.find(" ")

    first_name = name_input[:first_name_index]
    print("first name:", first_name)


# UNCOMMENT EACH FUNCTION INIVIDUALLY TO TEST:
# chapter_1()
# chapter_2()
# chapter_3()
# chapter_4()
# chapter_5()
# chapter_6()
