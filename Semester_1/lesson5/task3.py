class Vector:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if isinstance(value, (int, float)):
            self._x = value
        raise ValueError("Значение должно быть числом")

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if isinstance(value, (int, float)):
            self._y = value
        raise ValueError("Значение должно быть числом")

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x + other._x, self._y + other._y)
        if isinstance(other, (int, float)):
            return Vector(self._x + other, self._y + other)
        raise ValueError(f"Сложение вектора с {type(other)} невозможно")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x - other._x, self._y - other._y)
        if isinstance(other, (int, float)):
            return Vector(self._x - other, self._y - other)
        raise ValueError(f"Вычитание из вектора с {type(other)} невозможно")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x * other._x, self._y * other._y)
        if isinstance(other, (int, float)):
            return Vector(self._x * other, self._y * other)
        raise ValueError(f"Умножение вектора на {type(other)} невозможно")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self._x == other._x and self._y == other._y
        raise ValueError(f"Сравнение вектора с {type(other)} невозможно")

    def __str__(self):
        return f'Vector({self._x}, {self._y})'

    def __repr__(self):
        return f'Vector(x={self._x}, y={self._y})'


if __name__ == '__main__':
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
