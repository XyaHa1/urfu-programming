import math


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value > 0:
            self._radius = value
            return
        raise ValueError("Радиус должен быть положительным числом")

    @property
    def area(self):
        return math.pi * self._radius ** 2


if __name__ == '__main__':
    circle = Circle(5)
    print(f"Радиус: {circle.radius}")
    print(f"Площадь: {circle.area}")
    circle.radius = 10
    print(f"Площадь: {circle.area}")
