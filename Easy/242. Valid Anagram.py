class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frq: list[int] = [0 for _ in range(128 * 2)]
        for i in range(0, len(s)):
            frq[ord(s[i])] += 1
            frq[ord(t[i]) + 128] += 1

        for i in range(0, 128):
            if frq[i] != frq[i + 128]:
                return False

        return True
