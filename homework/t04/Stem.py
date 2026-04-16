from Figure import Figure
from turtle import *


class Stem(Figure):
    def __init__(self, x, y, length, color):
        super().__init__(x, y, color)
        self.length = length

    def draw(self):
        up()
        goto(self.x, self.y)

        pensize(5)
        pencolor(self.color)
        down()
        setheading(270)
        forward(self.length)


if __name__ == '__main__':
    s = Stem(0, 0, 100, "pink")
    s.show()

    mainloop()