class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x[0])
        newIntervals: list[list[int]] = []
        start: int = 0
        end: int = start
        i: int = end
        while i < len(intervals):
            i += 1
            while i < len(intervals) and intervals[end][1] >= intervals[i][0]:
                if intervals[end][1] <= intervals[i][1]:
                    end = i
                i += 1
            newIntervals.append([intervals[start][0], intervals[end][1]])
            start = end = i
        return newIntervals
