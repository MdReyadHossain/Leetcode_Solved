import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        pattern: str = r'^[^a-zA-Z0-9]+$'
        leftPtr: int = 0
        rightPtr: int = len(s) - 1
        while leftPtr < rightPtr:
            if re.fullmatch(pattern, s[leftPtr]):
                leftPtr += 1
                continue
            elif re.fullmatch(pattern, s[rightPtr]):
                rightPtr -= 1
                continue
            if s[leftPtr].upper() == s[rightPtr].upper():
                leftPtr += 1
                rightPtr -= 1
            elif s[leftPtr].upper() != s[rightPtr].upper():
                return False
        return True
