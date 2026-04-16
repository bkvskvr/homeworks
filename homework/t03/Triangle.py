import math
from Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c

    def square(self):
        p = (self.a + self.b + self.c) / 2

        val = p * (p - self.a) * (p - self.b) * (p - self.c)
        if val <= 0:
            return 0
        return math.sqrt(val)

    def volume(self):
        return self.square()

