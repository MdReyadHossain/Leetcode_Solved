class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums) <= 1:
            return True
        reach: bool = True
        target = len(nums) - 1
        place = target - 1
        while place >= 0:
            if target - place <= nums[place]:
                target = place
                place = target - 1
                reach = True
            else:
                place -= 1
                reach = False
        return reach
