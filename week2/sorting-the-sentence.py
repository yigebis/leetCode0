class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        order = [""]*len(words)
        for word in words:
            order[int(word[-1]) - 1] = word[:-1]
        return " ".join(order)
        