class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        freq = {}
        cnt = 0
        for i in range(0, len(nums)):
            value: int = nums[i]
            if value not in freq:
                freq[value] = 1

        for i in range(0, len(nums)):
            value = nums[i]
            if (value - 1) not in freq:
                cnt += 1
                while (value + 1) in freq:
                    value += 1
                    cnt += 1
            freq[nums[i]] = cnt
            cnt: int = 0

        for num in freq:
            if cnt < freq[num]:
                cnt = freq[num]

        return cnt
