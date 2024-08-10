class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totalGas: int = sum(gas)
        totalCost: int = sum(cost)
        tank: int = 0
        index: int = -1
        if totalCost > totalGas:
            return index

        for i in range(0, len(gas)):
            if tank + (gas[i] - cost[i]) < 0:
                tank = 0
                index = -1
            else:
                tank += (gas[i] - cost[i])
                if index == -1:
                    index = i
        return index
