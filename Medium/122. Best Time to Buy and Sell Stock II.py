class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        leftPtr: int = 0
        rightPtr: int = 1
        sum: int = 0
        while rightPtr < len(prices):
            if prices[leftPtr] < prices[rightPtr]:
                if rightPtr >= len(prices) - 1:
                    sum += (prices[rightPtr] - prices[leftPtr])
                    break
                elif prices[rightPtr] > prices[rightPtr + 1]:
                    sum += (prices[rightPtr] - prices[leftPtr])
                    leftPtr = rightPtr + 1
                    rightPtr = leftPtr + 1
                else:
                    rightPtr += 1
            else:
                leftPtr = rightPtr
                rightPtr = leftPtr + 1

        return sum
