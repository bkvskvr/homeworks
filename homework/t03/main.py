from Triangle import Triangle
from Rectangle import Rectangle
from Circle import Circle
from Trapeze import Trapeze
from Parallelogram import Parallelogram
from Ball import Ball
from TriangularPyramid import TriangularPyramid
from QuadrangularPyramid import QuadrangularPyramid
from RectangularParallelepiped import RectangularParallelepiped
from Cone import Cone
from TriangularPrism import TriangularPrism

def main():
    classes_map = {
        "Triangle": Triangle,
        "Rectangle": Rectangle,
        "Trapeze": Trapeze,
        "Parallelogram": Parallelogram,
        "Circle": Circle,
        "Ball": Ball,
        "TriangularPyramid": TriangularPyramid,
        "QuadrangularPyramid": QuadrangularPyramid,
        "RectangularParallelepiped": RectangularParallelepiped,
        "Cone": Cone,
        "TriangularPrism": TriangularPrism
    }

    figures = []

    try:
        with open("../t02/input01.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split()
                if not parts:
                    continue

                shape_name = parts[0]
                params = [float(p) for p in parts[1:]]

                if shape_name in classes_map:
                    shape_class = classes_map[shape_name]
                    figure_instance = shape_class(*params)
                    figures.append((shape_name, figure_instance))

    except FileNotFoundError:
        print("Помилка: Файл input01.txt не знайдено.")
        return

    if not figures:
        print("Список фігур порожній.")
        return

    max_figure = figures[0]
    for fig_name, fig_obj in figures:
        if fig_obj.volume() > max_figure[1].volume():
            max_figure = (fig_name, fig_obj)

    print(f"Фігура з найбільшою мірою: {max_figure[0]}")
    print(f"Міра: {max_figure[1].volume():.2f}")


if __name__ == '__main__':
    main()