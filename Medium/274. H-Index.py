class Solution:
    def hIndex(self, citations: list[int]) -> int:
        citations.sort(reverse=True)
        index: int = 0
        for i in range(0, len(citations) + 1):
            for j in range(len(citations)):
                if i > citations[j]:
                    n: int = len(citations)
                    while j < n:
                        citations.pop()
                        j += 1
                    break
            if i <= len(citations):
                index = i
            else:
                return index
        return index
