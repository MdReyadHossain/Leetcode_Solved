class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        found = False
        for i in range(len(nums)):
            if nums[i] >= target:
                found = True
                return i

        if found == False:
            return len(nums)
