class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        diffNum: int = None
        cnt: int = 0
        for i in range(0, len(nums)):
            if diffNum != nums[i]:
                diffNum = nums[i]
                nums[cnt] = diffNum
                cnt += 1

        return cnt
