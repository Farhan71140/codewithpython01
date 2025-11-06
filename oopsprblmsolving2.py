'''Question:Create a class Rectangle with attributes length and width. Add methods to calculate area() and perimeter()'''
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Create a rectangle object
rect1 = Rectangle(10, 5)

# Calculate and print area and perimeter
print("Area:", rect1.area())         # Output: Area: 50
print("Perimeter:", rect1.perimeter())  # Output: Perimeter: 30
