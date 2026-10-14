# Instance methods: Rectangle area and perimeter
# Problem: Create a rectangle class with length and breadth

class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)
rectangle1 = Rectangle(5,3)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())