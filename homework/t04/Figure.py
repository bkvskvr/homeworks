import abc
from turtle import *


class Figure(metaclass=abc.ABCMeta):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.is_visible = False

    @abc.abstractmethod
    def draw(self):
        pass

    def is_shown(self):
        return self.is_visible

    def show(self):
        if not self.is_visible:
            self.is_visible = True
            self.draw()

    def colour(self, new_color):
        self.color = new_color

    def hide(self):
        if self.is_visible:
            old_color = self.color
            self.colour("white")
            self.draw()
            self.colour(old_color)
            self.is_visible = False

    def move(self, dx, dy):
        self.hide()
        self.x += dx
        self.y += dy
        self.show()








