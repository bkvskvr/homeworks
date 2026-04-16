from Figure import Figure
from turtle import *


class Petal(Figure):
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
        circle(self.size, 120)
        left(60)
        circle(self.size, 120)
        left(60)
        end_fill()

if __name__ == '__main__':
    p = Petal(10, 0, 50, "#FADADD", 30)
    p.show()

    mainloop()