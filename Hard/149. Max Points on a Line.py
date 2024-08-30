class Solution:
    def lineEq(self, point1: list[int], point2: list[int]) -> str:
        if point2[0] == point1[0]:
            return f"x{point1[0]}"

        elif point2[1] == point1[1]:
            return f"y{point1[1]}"

        slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
        intercept = point1[1] - slope * point1[0]

        if intercept >= 0:
            return f"{slope}x + {intercept}"
        else:
            return f"{slope}x - {abs(intercept)}"

    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1
        slops = {}
        max: int = 0
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                if j == i:
                    continue
                key: str = self.lineEq(points[i], points[j])
                if key not in slops:
                    slops[key] = [points[j]]
                elif points[j] not in slops[key]:
                    slops[key].append(points[j])

                if points[i] not in slops[key]:
                    slops[key].append(points[i])

        for slop in slops:
            if max < len(slops[slop]):
                max = len(slops[slop])
        return max