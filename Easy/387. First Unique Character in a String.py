class Solution:
    def firstUniqChar(self, s: str) -> int:
        frquency: list[int] = [0] * 27
        for c in s:
            frquency[ord(c) - 96] += 1

        for i in range(len(s)):
            if frquency[ord(s[i]) - 96] == 1:
                return i
        return -1
