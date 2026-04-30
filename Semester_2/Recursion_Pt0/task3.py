class FastPower:

    @staticmethod
    def power_recursive(base: float, exponent: int) -> float:
        if base == 0:
            raise ValueError()
        
        if exponent == 0:
            return 1
        
        if exponent < 0:
            return 1.0 / FastPower.power_recursive(base, -exponent)
        
        if exponent % 2 == 0:
            return FastPower.power_recursive(base * base, exponent // 2)

        return base * FastPower.power_recursive(base, exponent - 1)

    @staticmethod
    def power_iterative(base: float, exponent: int) -> float:
        if base == 0:
            raise ValueError()
        
        if exponent == 0:
            return 1
        
        if exponent < 0:
            exponent = -exponent
            base = 1 / base

        r = 1
        while exponent > 0:
            if exponent % 2 == 0:
                base *= base
                exponent //= 2
            else:
                r *= base
                exponent -= 1
        return r


if __name__ == "__main__":
    print(FastPower.power_recursive(2, -3))