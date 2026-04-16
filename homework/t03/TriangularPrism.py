from Triangle import Triangle
class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
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
        return super().perimetr() * self.height()

    def volume(self):
        return self.squareBase() * self.height()

