class Solution:
    def intToRoman(self, num: int) -> list[str]:
        roman: str = "M" * int(num / 1000)
        num = num - (1000 * int(num / 1000))
        if int(num / 100) < 4:
            roman += "C" * int(num / 100)
        elif int(num / 100) == 9:
            roman += "CM"
        elif int(num / 100) == 4:
            roman += "CD"
        elif int(num / 100) > 4:
            roman += "D"
            roman += "C" * (int(num / 100) - 5)

        num = num - (100 * int(num / 100))
        if int(num / 10) < 4:
            roman += "X" * int(num / 10)
        elif int(num / 10) == 9:
            roman += "XC"
        elif int(num / 10) == 4:
            roman += "XL"
        elif int(num / 10) > 4:
            roman += "L"
            roman += "X" * (int(num / 10) - 5)

        num = num - (10 * int(num / 10))
        if num < 4:
            roman += "I" * num
        elif num == 9:
            roman += "IX"
        elif num == 4:
            roman += "IV"
        elif num > 4:
            roman += "V"
            roman += "I" * (num - 5)
        return roman
