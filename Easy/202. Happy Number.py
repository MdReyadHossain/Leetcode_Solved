class Solution:
    def seperateDigit(self, n: int) -> list[int]:
        digits: list[int] = []
        while n > 0:
            digits.append(n % 10)
            n = int(n / 10)
        return digits

    def isHappy(self, n: int) -> bool:
        hashTable = {}
        mul: int = 0
        while n > 1:
            digits: list[int] = self.seperateDigit(n)
            for i in range(len(digits)):
                mul += digits[i] * digits[i]
            n = mul
            mul = 0
            if n in hashTable:
                return False
            hashTable[n] = 1
        return True