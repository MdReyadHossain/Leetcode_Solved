class Solution:
    def isPalindrom(self, word: str) -> bool:
        leftPtr: int = 0
        rightPtr: int = len(word) - 1
        while leftPtr < rightPtr:
            if word[leftPtr] != word[rightPtr]:
                return False
            leftPtr += 1
            rightPtr -= 1

        return True

    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.isPalindrom(word):
                return word
        return ""
