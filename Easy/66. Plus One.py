class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        carry: bool = True

        for i in range(len(digits) - 1, -1, -1):
            if carry:
                sum = digits[i] + 1
                if sum < 10:
                    carry = False
                    digits[i] = sum
                else:
                    digits[i] = 0
        if carry:
            return [1] + digits
        else:
            return digits
