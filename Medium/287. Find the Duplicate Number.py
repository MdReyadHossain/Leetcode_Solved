class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        arr: list = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            if arr[nums[i]] == 0:
                arr[nums[i]] = 1
            else:
                return nums[i]
