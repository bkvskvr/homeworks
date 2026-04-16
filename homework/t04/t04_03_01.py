import random
from turtle import *
from Flower import Flower

speed(0)
hideturtle()
bgcolor("white")

colors = ["pink", "lightpink", "#FFB6C1", "plum", "#FADADD"]

positions = [(-200, 50), (-100, -50), (0, 80), (100, -30), (200, 60)]

for x, y in positions:
    col = random.choice(colors)
    f = Flower(x, y, col)
    f.show()

mainloop()