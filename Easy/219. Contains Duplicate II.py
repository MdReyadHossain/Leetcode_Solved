class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        freq = {}
        for i in range(0, len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = i
                continue
            if i - freq[nums[i]] <= k:
                return True
            freq[nums[i]] = i

        return False
