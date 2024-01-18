class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        cnt: int = 1
        index: int = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1] and cnt >= 2:
                cnt += 1
            elif nums[i] == nums[i+1] and cnt < 2:
                nums[index] = nums[i + 1]
                cnt += 1
                index += 1
            else:
                nums[index] = nums[i + 1]
                cnt = 1
                index += 1

        return index
