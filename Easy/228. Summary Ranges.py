class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        left: int = 0
        right: int = 0
        result: list[str] = []
        i: int = 0
        while i < len(nums):
            left = nums[i]
            right = left
            i += 1
            if i == len(nums):
                result.append(f'{left}')
                break
            while nums[i] - nums[i-1] == 1:
                right = nums[i]
                i += 1
                print(right)
                if i == len(nums):
                    break
            if right - left > 0:
                result.append(f'{left}->{right}')
            else:
                result.append(f'{left}')

        return result
