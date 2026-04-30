class Matrix2x2:
    def __init__(self, a: int, b: int, c: int, d: int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __mul__(self, other: 'Matrix2x2') -> 'Matrix2x2':
        if not isinstance(other, Matrix2x2):
            raise TypeError("Other must be a Matrix2x2")
        
        return Matrix2x2(
            self.a * other.a + self.b * other.c,
            self.a * other.b + self.b * other.d,
            self.c * other.a + self.d * other.c,
            self.c * other.b + self.d * other.d,
        )

    def power(self, n: int) -> 'Matrix2x2':
        result = Matrix2x2(1, 0, 0, 1)
        if n == 0:
            return result
        
        if n % 2 == 0:
            return self.power(n // 2) * self.power(n // 2)
        
        return self * self.power(n - 1)

    def __repr__(self) -> str:
        return f"[[{self.a}, {self.b}], [{self.c}, {self.d}]]"


class PopularityPredictor:
    def __init__(self):
        self.transformation = Matrix2x2(1, 1, 1, 0)

    def predict(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be non-negative")
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        return self.transformation.power(n - 1).a


if __name__ == "__main__":
    print(PopularityPredictor().predict(6))