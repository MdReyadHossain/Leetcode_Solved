class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product: int = 1
        num: int = 0
        cnt: int = 0
        for num in nums:
            if num == 0:
                cnt += 1
                continue
            product *= num

        for i in range(0, len(nums)):
            if cnt > 1 or (cnt == 1 and nums[i] != 0):
                nums[i] = 0
                continue
            if nums[i] == 0:
                num = product
            else:
                num = (int)(product / nums[i])
            nums[i] = num

        return nums
