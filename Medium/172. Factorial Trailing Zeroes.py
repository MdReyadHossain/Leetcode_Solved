class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        cnt: int = 0
        while int(n / 5) != 0:
            cnt += int(n / 5)
            n //= 5
        return cnt