class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return x
        left: int = 0
        right: int = x
        mid = right

        while right - left != 1:
            mid = left + int((right - left) / 2)
            if mid * mid == x:
                return mid

            elif mid * mid > x:
                right = mid

            else:
                left = mid

        return left
