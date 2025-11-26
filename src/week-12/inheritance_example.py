class Animal:
    def __init__(self, name, species):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

    def move(self):
        return f"{self.name} moves around"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Canine")

        self.breed = breed
        print(f"Dog xconstructor: breed is {breed}")

    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


chance = Dog("Chance", "Shih Tzu", "dog")
carl = Cat("Carl")

print(chance.speak())
print(carl.speak())
