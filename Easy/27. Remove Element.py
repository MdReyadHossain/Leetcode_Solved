class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        cnt: int = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[cnt] = nums[i]
                cnt += 1
        
        return cnt