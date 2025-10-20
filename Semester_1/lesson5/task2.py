class Quadrilateral:
    def __init__(self, name, height, width, color):
        self.name = name
        self.height = height
        self.width = width
        self.color = color

    def get_area(self):
        pass

    def get_perimeter(self):
        pass


class Rectangle(Quadrilateral):
    def __init__(self, name, height, width, color):
        super().__init__(name, height, width, color)

    def get_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** 0.5

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)


class Square(Quadrilateral):
    def __init__(self, name, height, width, color):
        super().__init__(name, height, width, color)

    def get_diagonal(self):
        return self.height * 2 ** 0.5

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 4 * self.height
