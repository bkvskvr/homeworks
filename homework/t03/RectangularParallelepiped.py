from Rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
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
        return 2 * (self.a + self.b) * self.height()

    def volume(self):
        return self.squareBase() * self.height()
