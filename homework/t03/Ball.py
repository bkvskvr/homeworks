import math
from Figure import Figure


class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self):
        return 3

    def squareSurface(self):
        return 4 * math.pi * (self.r ** 2)

    def volume(self):
        return (4 / 3) * math.pi * (self.r ** 3)
