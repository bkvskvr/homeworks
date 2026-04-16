from turtle import *
import random

class Stem:
    def __init__(self, t):
        self.t = t

    def draw(self, length, color="dark green", thickness=4):
        self.t.pensize(thickness)
        self.t.color(color)
        self.t.right(90)
        self.t.forward(length)
        self.t.backward(length)
        self.t.left(90)

class Leaf:
    def __init__(self, t):
        self.t = t

    def draw(self, size=40, color="green"):
        self.t.color(color)
        self.t.begin_fill()
        self.t.circle(size, 90)
        self.t.left(90)
        self.t.circle(size, 90)
        self.t.left(90)
        self.t.end_fill()

class Petal:
    def __init__(self, t):
        self.t = t

    def draw(self, radius, color="red"):
        self.t.color(color)
        self.t.begin_fill()
        self.t.circle(radius, 60)
        self.t.left(120)
        self.t.circle(radius, 60)
        self.t.left(120)
        self.t.end_fill()

class Flower:
    def __init__(self, t):
        self.t = t
        self.stem = Stem(t)
        self.leaf = Leaf(t)
        self.petal = Petal(t)

    def draw(self, x, y, stem_length=150, petal_radius=70, petal_color="red"):
        self.t.penup()
        self.t.goto(x, y)
        self.t.pendown()
        self.t.setheading(0)
        self.stem.draw(stem_length)
        self.t.penup()
        self.t.right(90)
        self.t.forward(stem_length // 2)
        self.t.left(90)
        self.t.pendown()
        self.leaf.draw()
        self.t.penup()
        self.t.left(90)
        self.t.forward(stem_length // 2)
        self.t.right(90)
        self.t.pendown()

        for _ in range(6):
            self.petal.draw(petal_radius, petal_color)
            self.t.right(60)

def main():
    screen = Screen()
    screen.bgcolor("white")
    screen.title("букет")

    t = Turtle()
    t.speed(0)

    my_flower = Flower(t)

    bouquet = [
        (-150, 0, "dark red"),
        (0, 50, "red"),
        (150, -20, "maroon"),
        (-70, -100, "crimson"),
        (80, -80, "firebrick")
    ]

    for x, y, color in bouquet:
        radius = random.randint(50, 80)
        my_flower.draw(x, y, petal_color=color, petal_radius=radius)

    t.hideturtle()
    done()

main()