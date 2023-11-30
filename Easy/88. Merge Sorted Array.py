class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        index1 = 0
        index2 = 0
        mergeList: list[int] = []
        while index1 < m and index2 < n:
            if nums1[index1] < nums2[index2]:
                mergeList.append(nums1[index1])
                index1 += 1
            else:
                mergeList.append(nums2[index2])
                index2 += 1

        while index1 < m:
            mergeList.append(nums1[index1])
            index1 += 1

        while index2 < n:
            mergeList.append(nums2[index2])
            index2 += 1

        for i in range(len(mergeList)):
            nums1[i] = mergeList[i]
