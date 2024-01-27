class Solution:
    def skipSameElementToRight(self, nums: list[int], index: int):
        while nums[index] == nums[index - 1] and index < len(nums) - 1:
            index += 1
        return index

    def skipSameElementToLeft(self, nums: list[int], index: int):
        while nums[index] == nums[index + 1] and index > 0:
            index -= 1
        return index

    def threeSum(self, nums: list[int]) -> list[list[int]]:  # O(n^2)
        nums.sort()  # O(nlogn)
        firstPrt: int = 0
        left: int = 0
        right: int = len(nums) - 1
        result: list = []
        print(nums)
        while firstPrt < len(nums) - 2:  # O(n^2)
            left = firstPrt + 1
            right = len(nums) - 1
            while left < right:
                if nums[firstPrt] + nums[left] + nums[right] > 0:
                    right -= 1
                    right = self.skipSameElementToLeft(nums, right)
                elif nums[firstPrt] + nums[left] + nums[right] < 0:
                    left += 1
                    left = self.skipSameElementToRight(nums, left)
                else:
                    result.append([nums[firstPrt], nums[left], nums[right]])
                    left += 1
                    left = self.skipSameElementToRight(nums, left)
            firstPrt += 1
            firstPrt = self.skipSameElementToRight(nums, firstPrt)

        return result


class Solution:
    def skipSameElementToRight(self, nums: list[int], index: int, limit: int):
        while nums[index] == nums[index - 1] and index < len(nums) - 1 and index < limit:
            index += 1
        return index

    def skipSameElementToLeft(self, nums: list[int], index: int, limit: int):
        while nums[index] == nums[index + 1] and index > 0 and index > limit:
            index -= 1
        return index

    def threeSum(self, nums: list[int]) -> list[list[int]]:  # O(n^2)
        nums.sort()  # O(nlogn)
        firstPrt: int = 0
        left: int = 0
        right: int = len(nums) - 1
        result: list = []
        print(nums)
        while firstPrt < len(nums) - 2:  # O(n^2)
            left = firstPrt + 1
            right = len(nums) - 1
            while left < right:
                if nums[firstPrt] + nums[left] + nums[right] > 0:
                    right -= 1
                    right = self.skipSameElementToLeft(nums, right, left)
                elif nums[firstPrt] + nums[left] + nums[right] < 0:
                    left += 1
                    left = self.skipSameElementToRight(nums, left, right)
                else:
                    result.append([nums[firstPrt], nums[left], nums[right]])
                    left += 1
                    left = self.skipSameElementToRight(nums, left, right)
            firstPrt += 1
            firstPrt = self.skipSameElementToRight(
                nums, firstPrt, len(nums) - 1)

        return result
