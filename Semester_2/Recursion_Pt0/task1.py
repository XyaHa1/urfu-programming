class FibonacciCalculator:
    def recursive_fibonacci(self, n: int) -> int:
        if n < 0:
            raise ValueError()
        if n == 0:
            return 0
        if n <= 2:
            return 1
        return self.recursive_fibonacci(n - 1) + self.recursive_fibonacci(n - 2)

    def iterative_fibonacci(self, n: int) -> int:
        if n < 0:
            raise ValueError()
        if n == 0:
            return 0
        if n <= 2:
            return 1
        dp = [1, 1]
        for i in range(2, n):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[-1]