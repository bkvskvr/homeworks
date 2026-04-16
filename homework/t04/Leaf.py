from Figure import Figure
from turtle import *


class Leaf(Figure):
    def __init__(self, x, y, size, color, angle):
        super().__init__(x, y, color)
        self.size = size
        self.angle = angle

    def draw(self):
        up()
        goto(self.x, self.y)

        setheading(self.angle)
        pensize(1)
        pencolor(self.color)
        fillcolor(self.color)
        begin_fill()
        down()
        circle(self.size, 90)
        left(90)
        circle(self.size, 90)
        left(90)
        end_fill()

if __name__ == '__main__':
    l = Leaf(0, -60, 30, "", 30)
    l.show()

    mainloop()