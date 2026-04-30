class PowerCalculator:
    @staticmethod
    def recursive(base: float, exponent: int) -> float:
        if base == 0:
            raise ValueError()
        
        if exponent == 0:
            return 1
        if exponent < 0:
            return 1 / PowerCalculator.recursive(base, -exponent)
        return base * PowerCalculator.recursive(base, exponent - 1)

    @staticmethod
    def iterative(base: float, exponent: int) -> float:
        if base == 0:
            raise ValueError()

        if exponent == 0:
            return 1
        
        neg = exponent < 0
        exponent = abs(exponent)

        r = base
        for _ in range(1, exponent):
            r *= base

        return 1 / r if neg else r
    

if __name__ == '__main__':
    print(PowerCalculator.iterative(2, 2))
