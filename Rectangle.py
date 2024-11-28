import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * self.width + 2 * self.height
    def diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)
    def __str__(self):
        return f'a: {self.width}, b: {self.height}, ümbermõõt: {self.perimeter()}, pindala: {self.diagonal()},'f'diagonaal: {self.diagonal()}'
