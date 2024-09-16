class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first: int = 1
        sec: int = 2
        for i in range(3, n + 1):
            sum: int = first + sec
            first = sec
            sec = sum
        return sum
