class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left: int = 0
        right: int = len(numbers) - 1
        while left < right:
            if (numbers[left] + numbers[right] > target):
                right -= 1
            elif (numbers[left] + numbers[right] < target):
                left += 1
            else:
                return [left + 1, right + 1]
