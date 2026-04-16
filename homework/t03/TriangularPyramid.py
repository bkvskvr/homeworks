import math
from Triangle import Triangle


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
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
        apothem = math.sqrt(self.height()**2 + (self.a * math.sqrt(3) / 6)** 2)
        return 3 * (0.5 * self.a * apothem)

    def volume(self):
        return (1 / 3) * self.squareBase() * self.height()

