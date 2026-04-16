import math

class Triangle:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = float(a), float(b), float(c)
        self.name = "Трикутник"

    def get_perimeter(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0
        return self.a + self.b + self.c

    def get_area(self):
        if self.a + self.b <= self.c or self.a + self.c <= self.b or self.b + self.c <= self.a:
            return 0

        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

class Rectangle:
    def __init__(self, a, b):
        self.a, self.b = float(a), float(b)
        self.name = "Прямокутник"

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

class Trapeze:
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = float(a), float(b), float(c), float(d)
        self.name = "Трапеція"

    def get_perimeter(self):
        return self.a + self.b + self.c + self.d

    def get_area(self):
        if self.a == self.b:
            return self.a * self.c

        diff = abs(self.a - self.b)
        p = (diff + self.c + self.d) / 2

        under_root = p * (p - diff) * (p - self.c) * (p - self.d)
        if under_root < 0:
            return 0

        h = (2 / diff) * math.sqrt(under_root)
        return ((self.a + self.b) / 2) * h

class Parallelogram:
    def __init__(self, a, b, h):
        self.a, self.b, self.h = float(a), float(b), float(h)
        self.name = "Паралелограм"

    def get_perimeter(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.h

class Circle:
    def __init__(self, r):
        self.r = float(r)
        self.name = "Круг"

    def get_perimeter(self):
        return 2 * math.pi * self.r

    def get_area(self):
        return math.pi * (self.r ** 2)

def analyze_figures_from_file(filename):
    figures_list = []

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.split()
                if not parts:
                    continue

                fig_type = parts[0]
                params = parts[1:]

                if fig_type == "Triangle":
                    figures_list.append(Triangle(*params))
                elif fig_type == "Rectangle":
                    figures_list.append(Rectangle(*params))
                elif fig_type == "Trapeze":
                    figures_list.append(Trapeze(*params))
                elif fig_type == "Parallelogram":
                    figures_list.append(Parallelogram(*params))
                elif fig_type == "Circle":
                    figures_list.append(Circle(*params))

    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return

    if not figures_list:
        print("Файл порожній або не містить коректних даних.")
        return

    max_area_fig = max(figures_list, key=lambda f: f.get_area())
    max_perim_fig = max(figures_list, key=lambda f: f.get_perimeter())

    print(f"Фігура з найбільшою площею: {max_area_fig.name} (Площа: {max_area_fig.get_area():.2f})")
    print(f"Фігура з найбільшим периметром: {max_perim_fig.name} (Периметр: {max_perim_fig.get_perimeter():.2f})")

analyze_figures_from_file('input01.txt')