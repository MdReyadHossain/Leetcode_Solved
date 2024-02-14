class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        freq: list[str] = [0] * 128
        leftPtr: int = 0
        rightPtr: int = 0
        subLen: int = 1
        while rightPtr < len(s):
            freq[ord(s[rightPtr])] += 1
            while freq[ord(s[rightPtr])] > 1:
                if rightPtr - leftPtr > subLen:
                    subLen = (rightPtr - leftPtr)
                freq[ord(s[leftPtr])] -= 1
                leftPtr += 1
                if freq[ord(s[rightPtr])] < 2 and rightPtr - leftPtr + 1 > subLen:
                    subLen = rightPtr - leftPtr + 1
            rightPtr += 1

        if (rightPtr - leftPtr) > subLen:
            subLen = (rightPtr - leftPtr)
        return subLen
