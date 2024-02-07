class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        leftPtr: int = 0
        rightPtr: int = 0
        sum: int = nums[leftPtr]
        subLength: int = float('inf')
        while rightPtr < len(nums):
            if sum >= target:
                if subLength == 1:
                    return subLength
                if (rightPtr - leftPtr) + 1 < subLength:
                    subLength = (rightPtr - leftPtr) + 1
                sum -= nums[leftPtr]
                leftPtr += 1
            else:
                rightPtr += 1
                if rightPtr < len(nums):
                    sum += nums[rightPtr]
        return 0 if subLength == float('inf') else subLength
