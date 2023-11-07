class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        index: int = -1
        cnt: int = 0
        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                k = i
                index = k
                for j in range(len(needle)):
                    if k > (len(haystack) - 1):
                        index = -1
                        break
                    if haystack[k] != needle[j]:
                        index = -1
                        break
                    k += 1
                    cnt += 1

                if cnt == len(needle):
                    return index
            cnt = 0
        return index
