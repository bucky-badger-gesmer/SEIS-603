class Dog:
    def __init__(self, name=None, age=None):
        if name == None:
            self.name = "Fido"

        if age == None:
            self.age = 11

        else:
            self.name = "Fido"
            self.age = 11

    def description(self):
        return f"{self.name} is {self.age} years old"

    def __def__(self):
        print("I am destroyed")


my_dog = Dog()

print(my_dog.description())
print(dir(my_dog))

buddy = Dog("Buddy")
miles = Dog("Miles", 4)

print(my_dog)
print(buddy)
print(miles)
