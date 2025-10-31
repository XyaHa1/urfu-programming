class Circle:
    _pi = 3.14

    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def pi(self):
        return self._pi

    def calculate_area(self):
        return self._pi * self._radius ** 2


class CalculateCircleLengthMixin(Circle):
    def calculate_length(self):
        return super().radius * super().pi * 2


class CircleWithMixin(CalculateCircleLengthMixin, Circle):
    pass


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
