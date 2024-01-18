class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bi: int = 0
        maxProfit: int = 0
        for si in range(len(prices)):
            if (prices[si] - prices[bi]) > maxProfit:
                maxProfit = prices[si] - prices[bi]
            elif prices[si] < prices[bi]:
                bi = si

        return maxProfit
