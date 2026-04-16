import math
from Rectangle import Rectangle


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
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
        h_a = math.sqrt(self.height()**2 + (self.b / 2)**2)
        h_b = math.sqrt(self.height()**2 + (self.a / 2)**2)
        return 2 * (0.5 * self.a * h_a) + 2 * (0.5 * self.b * h_b)

    def volume(self): return (1 / 3) * self.squareBase() * self.height()