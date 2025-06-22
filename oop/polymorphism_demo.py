# polymorphism_demo.py
import math

class Shape:
    def area(self):
        """Abstract method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area() method")


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of a rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate the area of a circle."""
        return math.pi * (self.radius ** 2)
    
# main.py
from polymorphism_demo import Shape, Rectangle, Circle


def main():
    # Create a list of shapes
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Rectangle(4, 6),
        Circle(3)
    ]

    # Demonstrate polymorphism
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")


if __name__ == "__main__":
    main()