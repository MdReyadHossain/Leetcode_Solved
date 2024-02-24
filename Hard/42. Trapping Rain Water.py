class Solution:
    def minLeftRight(self, maxLeft: list[int], maxRight: list[int], minLR: list[int]) -> list[int]:
        for i in range(len(minLR)):
            minLR[i] = min(maxLeft[i], maxRight[i])
        return minLR

    def trap(self, height: list[int]) -> int:
        sum: int = 0
        left: int = 0
        right: int = 0
        j: int = len(height) - 1
        maxLeft: list[int] = [0] * len(height)
        maxRight: list[int] = [0] * len(height)
        minLR: list[int] = [0] * len(height)
        for i in range(len(height)):
            maxLeft[i] = left
            maxRight[j] = right
            if left < height[i]:
                left = height[i]
            if right < height[j]:
                right = height[j]
            j -= 1
        self.minLeftRight(maxLeft, maxRight, minLR)

        for i in range(len(height)):
            if minLR[i] - height[i] > 0:
                sum += minLR[i] - height[i]
        return sum
