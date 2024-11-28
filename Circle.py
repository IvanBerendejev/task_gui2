import math

class Circle:

    def __init__(self, radius): # Konstruktor käivitakse obkekti loomisel
        self.radius = radius # loome klassisisese muutuja
        # print(radius)
    def diameter(self):
        return 2 * self.radius
    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return (f'Raadius: {self.radius}\nDiameeter: {self.diameter()}\n'
                f'Pindala: {self.area()}\nÜmbermõõt: {self.circumference()}')

#import random  delal sam
    #radius = [random.uniform(1, 10) for _ in range(5)] delal sam


