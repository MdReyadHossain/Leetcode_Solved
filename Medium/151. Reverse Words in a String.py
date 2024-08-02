class Solution:
    def reverseWords(self, s: str) -> str:
        if s == " " or s == "":
            return ""

        words: list[str] = []
        word: str = ""
        for letter in s:
            if letter == " ":
                if word != "":
                    words.append(word)
                    word = ""
                continue
            word += letter

        if word != "":
            words.append(word)
            word = ""

        s = ""
        for i in range(len(words) - 1, 0, -1):
            s += words[i] + " "
        s += words[0]
        return s
    

class Solution:
    def reverseWords(self, s: str) -> str:
        words: list[str] = s.split()
        s = ""
        for i in range(len(words) - 1, 0, -1):
            s += words[i] + " "
        s += words[0]
        return s