import math
from Figure import Figure


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def dimention(self):
        return 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        if self.a == self.b:
            return self.a * self.c
        try:
            val = (self.a - self.b)
            2 + self.c**2 - self.d ** 2
            h_sq = self.c**2 - (val / (2 * (self.a - self.b)))
            2
            return ((self.a + self.b) / 2) * math.sqrt(h_sq)
        except ValueError:
            return 0

    def volume(self):
        return self.square()
