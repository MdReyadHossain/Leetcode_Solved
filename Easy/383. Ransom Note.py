class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap: list[int] = [0] * 128
        for letter in magazine:
            hashMap[ord(letter)] += 1
        for letter in ransomNote:
            hashMap[ord(letter)] -= 1
            if hashMap[ord(letter)] < 0:
                return False
        return True
