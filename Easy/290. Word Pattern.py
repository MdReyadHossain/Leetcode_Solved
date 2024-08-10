class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList: list = s.split(' ')
        if len(sList) != len(pattern):
            return False
        freq: list[str] = ['-' for _ in range(129)]

        for i in range(len(pattern)):
            if freq[ord(pattern[i])] == '-':
                for word in freq:
                    if word == sList[i]:
                        return False
                freq[ord(pattern[i])] = sList[i]

            elif freq[ord(pattern[i])] != sList[i]:
                return False

        return True
