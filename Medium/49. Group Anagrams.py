class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}
        key: str = ''
        for word in strs:
            key = f'{sorted(word)}'
            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key] = [word]
        return list(anagram.values())
    

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagram = {}
        key: str = ''
        freq: list[int] = [0 for _ in range(128)]
        for word in strs:
            for letter in word:
                freq[ord(letter)] += 1
            for i in range(128):
                if freq[i] > 0:
                    key += f'{freq[i]}{chr(i)}'

            if key in anagram:
                anagram[key].append(word)
            else:
                anagram[key] = [word]
            freq = [0 for _ in range(128)]
            key = ''
        return list(anagram.values())