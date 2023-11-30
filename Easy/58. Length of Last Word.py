class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sList: list = s.split()
        lastWord: str = sList[len(sList) - 1]
        return len(lastWord)
