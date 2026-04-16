from turtle import*
from Figure import Figure
from Center import Center
from Stem import Stem
from Leaf import Leaf
from Petal import Petal

class Flower(Figure):
    def __init__(self, x, y, petal_color):
        super().__init__(x, y, petal_color)

        self.stem = Stem(x, y, 150, "green")
        self.center = Center(x, y, 15, "yellow")
        self.petals = []

        for angle in range(0, 360, 60):
            self.petals.append(Petal(x, y, 40, petal_color, angle))

        self.leaves = []
        self.leaves.append(Leaf(x, y -70 ,30, "green", 0))
        self.leaves.append(Leaf(x, y -90, 30, "green", 180))

    def draw(self):
        self.stem.draw()

        for leaf in self.leaves:
            leaf.draw()

        for petal in self.petals:
            petal.draw()

        self.center.draw()

if __name__ == '__main__':
    speed(0)

    f = Flower(0, 0, "lightpink")
    f.show()

    mainloop()
