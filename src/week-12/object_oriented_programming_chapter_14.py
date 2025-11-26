import random


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)

    def display(self):
        print("=" * 50)
        print("RECTANGLE INFORMATION")
        print("=" * 50)

        print(f"Dimensions: {self.length} (length), {self.width} (width)")
        print(f"Area: {self.area()}")
        print(f"Perimeter: {self.perimeter()}\n")


my_rectangles: list[Rectangle] = []

# Create 7 random rectangles:
for i in range(0, 7):
    l = random.randint(1, 10)
    a = random.randint(1, 10)

    my_rectangle = Rectangle(l, a)
    my_rectangles.append(my_rectangle)

for i in range(0, len(my_rectangles)):
    my_rectangles[i].display()
