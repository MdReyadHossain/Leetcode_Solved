class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s
        res = ''
        for i in range(len(s) - 2):
            if s[i] == s[i + 1] and s[i + 2] == s[i + 1]:
                continue
            res += s[i]
        res += s[-2]
        res += s[-1]

        return res
