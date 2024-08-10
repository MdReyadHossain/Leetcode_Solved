class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxWater: int = 0
        left: int = 0
        right: int = len(height) - 1
        while left < right:
            length: int = right - left
            water: int = length * min(height[left], height[right])
            maxWater = max(maxWater, water)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
