import math

class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def hypotenuse(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    def area(self):
        return 1/2 * self.a * self.b

    def perimeter(self):
        return self.a + self.b + self.hypotenuse()

    def __repr__(self):
        return (f"Külg a: {self.a}\nKülg b: {self.b}\n"
                f"hüpotenuus: {self.hypotenuse()}\nPindala: {self.area()}\n"
                f"Ümbermõõt: {self.perimeter()}")