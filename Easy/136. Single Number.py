class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res: int = 0
        for num in nums:
            res ^= num

        return res
