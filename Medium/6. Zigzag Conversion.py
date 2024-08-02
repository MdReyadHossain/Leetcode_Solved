import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        res: str = ""
        col: int = math.ceil(len(s) / 2)
        arr: list[list[str]] = [
            [0 for _ in range(col)] for _ in range(numRows)]
        index: int = -1
        i: int = -1
        j: int = 0
        while index + 1 < len(s):
            while i + 1 < numRows and index + 1 < len(s):
                i += 1
                index += 1
                arr[i][j] = s[index]
            while i - 1 >= 0 and index + 1 < len(s):
                i -= 1
                j += 1
                index += 1
                arr[i][j] = s[index]

        for i in range(0, numRows):
            for j in range(0, col):
                if arr[i][j] != 0:
                    res += arr[i][j]

        return res
