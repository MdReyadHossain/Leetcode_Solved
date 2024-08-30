class Solution:
    def solve(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            return self.solve(1 / x, -n)
        elif n % 2:
            return x * self.solve(x * x, (n - 1) / 2)

        return self.solve(x * x, n / 2)

    def myPow(self, x: float, n: int) -> float:
        return self.solve(x, n)
