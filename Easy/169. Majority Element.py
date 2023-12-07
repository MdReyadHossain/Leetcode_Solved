# time: O(n) space: O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result: int = 0
        cnt: int = 0
        for num in nums:
            if cnt == 0:
                result = num

            if result == num:
                cnt += 1
            else:
                cnt -= 1

        return result

# time: O(n) space: O(n)   X wrong


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq: list[int] = [0] * (len(nums) + 1)
        max: int = 0
        for num in nums:
            freq[num] += 1
            if freq[num] > max:
                max = freq[num]
                index = num

        return index
