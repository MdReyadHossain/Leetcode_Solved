class Solution:
    def triangleType(self, nums: list[int]) -> str:
        if nums[0] == 0 or nums[1] == 0 or nums[2] == 0:
            return 'none'

        if nums[0] + nums[1] > nums[2] and nums[0] + nums[2] > nums[1] and nums[1] + nums[2] > nums[0]:
            if nums[0] == nums[1] and nums[0] == nums[2]:
                return 'equilateral'
            elif nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
                return 'isosceles'
            else:
                return 'scalene'
        return 'none'
