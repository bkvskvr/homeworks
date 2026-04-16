from Figure import Figure
from turtle import *


class Center(Figure):
    def __init__(self, x, y, r, color):
        super().__init__(x, y, color)
        self.r = r

    def draw(self):
        up()
        setheading(0)
        goto(self.x, self.y - self.r)

        pensize(0)
        pencolor(self.color)
        fillcolor(self.color)
        begin_fill()
        down()
        circle(self.r)
        end_fill()

if __name__ == '__main__':
    c = Center(-5, 0, 10, "lightpink")
    c.show()

    mainloop()
