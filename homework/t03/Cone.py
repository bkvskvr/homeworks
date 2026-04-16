import math
from Circle import Circle


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self._h = h

    def dimention(self):
        return 3

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareBase(self):
        return super().square()

    def height(self):
        return self._h

    def squareSurface(self):
        l = math.sqrt(self.r**2 + self.height()**2)
        return math.pi * self.r * l

    def volume(self):
        return (1 / 3) * self.squareBase() * self.height()
