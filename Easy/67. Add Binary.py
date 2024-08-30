class Solution:
    def patternBinary(self, a: str, b: str, carry: str) -> str:
        pattern: str = ''
        for c in sorted([a, b, carry]):
            pattern += c
        if pattern == '000':
            return '00'
        elif pattern == '001':
            return '01'
        elif pattern == '011':
            return '10'
        elif pattern == '111':
            return '11'

    def addBinary(self, a: str, b: str) -> str:
        extra: int = abs(len(a) - len(b))
        res: list[str] = list(max(len(a), len(b)) * '0')
        carry: str = '0'
        if len(a) > len(b):
            b = extra * '0' + b
        elif len(a) < len(b):
            a = extra * '0' + a

        for i in range(len(a) - 1, -1, -1):
            output: str = self.patternBinary(a[i], b[i], carry)
            carry = output[0]
            res[i] = output[1]

        res = ''.join(res)
        if carry == '1':
            res = carry + res
        return res