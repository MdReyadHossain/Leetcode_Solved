class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left: int = 0
        right = len(matrix[0])
        up: int = 0
        down: int = len(matrix)
        cnt: int = 0
        spiral: list[int] = []
        while True:
            for i in range(left, right):
                if cnt == len(matrix) * len(matrix[0]):
                    return spiral
                cnt += 1
                spiral.append(matrix[up][i])

            up += 1
            for i in range(up, down):
                if cnt == len(matrix) * len(matrix[0]):
                    return spiral
                cnt += 1
                spiral.append(matrix[i][right - 1])

            right -= 1
            for i in range(right - 1, left - 1, -1):
                if cnt == len(matrix) * len(matrix[0]):
                    return spiral
                cnt += 1
                spiral.append(matrix[down - 1][i])

            down -= 1
            for i in range(down - 1, up - 1, -1):
                if cnt == len(matrix) * len(matrix[0]):
                    return spiral
                cnt += 1
                spiral.append(matrix[i][left])

            left += 1
            if cnt == len(matrix) * len(matrix[0]):
                return spiral
