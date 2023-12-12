class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        arr: list[int] = []
        n: int = len(nums)
        for i in range(n-(k % n), n):
            arr.append(nums[i])

        for i in range(n-(k % n)):
            arr.append(nums[i])

        for i in range(n):
            nums[i] = arr[i]
