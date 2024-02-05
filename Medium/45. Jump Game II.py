class Solution:
    def jump(self, nums: list[int]) -> bool:
        leftPtr: int = 0
        rightPtr: int = leftPtr + 1
        max: int = 0
        maxPtr: int = 0
        sum: int = 0
        while rightPtr < len(nums):
            limit: int = nums[leftPtr] + leftPtr
            while rightPtr <= limit and rightPtr < len(nums):
                if (nums[rightPtr] + rightPtr) >= max:
                    max = nums[rightPtr] + rightPtr
                    maxPtr = rightPtr
                rightPtr += 1
            leftPtr = maxPtr
            rightPtr = limit + 1
            sum += 1
        return sum
