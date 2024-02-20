class Solution:
    def candy(self, ratings: list[int]) -> int:
        freq: list[int] = [1] * len(ratings)
        for i in range(len(ratings) - 1):
            if ratings[i] > ratings[i + 1] and freq[i] <= freq[i + 1]:
                freq[i] = freq[i + 1] + 1
            elif ratings[i] < ratings[i + 1] and freq[i] >= freq[i + 1]:
                freq[i + 1] = freq[i] + 1

        for i in range(len(ratings)-1, 0, -1):
            if ratings[i] > ratings[i - 1] and freq[i] <= freq[i - 1]:
                freq[i] = freq[i-1] + 1
            elif ratings[i] < ratings[i - 1] and freq[i] >= freq[i - 1]:
                freq[i - 1] = freq[i] + 1

        return sum(freq)
