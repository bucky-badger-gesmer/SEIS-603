if __name__ == "__main__":
    name = input("What is your name?")
    email = input("What is your email?")
    phone = input("What is your phone number?")

    fname = "directory.txt"
    fhand = open(fname, "w")

    fhand.write("Name: " + name + "\n")
    fhand.write("Email: " + email + "\n")
    fhand.write("Phone: " + phone + "\n")

    fhand.close()

    fhand = open(fname)

    for cheese in fhand:
        cheese = cheese.rstrip()
        print(cheese)

    fhand.close()
