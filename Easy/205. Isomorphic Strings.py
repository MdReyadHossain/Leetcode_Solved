class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq: list[str] = [-1 for i in range(128)]
        for i in range(len(t)):
            index: int = ord(s[i])
            if freq[index] == -1:
                freq[index] = t[i]
            elif freq[index] != t[i]:
                return False

        freq: list[str] = [-1 for i in range(128)]
        for i in range(len(s)):
            index: int = ord(t[i])
            if freq[index] == -1:
                freq[index] = s[i]
            elif freq[index] != s[i]:
                return False

        return True
