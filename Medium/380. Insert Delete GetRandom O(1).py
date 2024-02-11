import random


class RandomizedSet:
    def __init__(self):
        self.numSet: list = []
        self.numMap: dict = {}  # val: index

    def insert(self, val: int) -> bool:
        if self.numMap.get(val) != None:
            return False

        self.numSet.append(val)
        self.numMap[val] = len(self.numSet) - 1
        return True

    def remove(self, val: int) -> bool:
        if self.numMap.get(val) != None:
            self.numSet[self.numMap[val]] = self.numSet[len(self.numSet) - 1]
            self.numMap[self.numSet[len(self.numSet) - 1]] = self.numMap[val]
            self.numSet.pop()
            self.numMap.pop(val)
            return True

        return False

    def getRandom(self) -> int:
        return random.choice(self.numSet)
