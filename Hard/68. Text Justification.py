import math


class Solution:
    def createLine(self, res: list[str], line: list[str], space: int):
        perLine: str = ""
        if len(line) == 1:
            line[0] += " " * space
        elif space % (len(line) - 1) == 0:
            for i in range(0, len(line) - 1):
                line[i] += " " * (space // (len(line) - 1))
                perLine += line[i]
        else:
            for i in range(0, len(line) - 1):
                x = math.ceil(space / (len(line) - 1 - i))
                line[i] += " " * x
                space -= x
                perLine += line[i]
        res.append(perLine + line[len(line) - 1])

    def fullJustify(self, words: list[str], maxWidth: int):
        letterCount: int = 0
        line: list[str] = []
        res: list[str] = []
        for i in range(len(words)):
            letterCount += len(words[i]) + 1
            if letterCount > maxWidth + 1:
                letterCount -= len(words[i]) + 1
                letter: int = letterCount - len(line)
                space: int = maxWidth - letter
                self.createLine(res, line, space)
                line = []
                letterCount = len(words[i]) + 1
            line.append(words[i])

            if i == len(words) - 1:
                space: int = maxWidth - (letterCount - len(line))
                perLine: str = ""
                for i in range(0, len(line) - 1):
                    line[i] += " "
                    perLine += line[i]
                    space -= 1
                res.append(perLine + line[len(line) - 1] + " " * space)
        return res
