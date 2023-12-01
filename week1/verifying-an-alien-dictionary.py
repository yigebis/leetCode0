class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        precedence = {}
        for i in range(len(order)):
            precedence[order[i]] = i

        def compare(word1, word2):
            i = 0
            while i < len(word1) and i < len(word2):
                if precedence[word1[i]] > precedence[word2[i]]:
                    return False
                elif precedence[word1[i]] < precedence[word2[i]]:
                    return True
                i += 1
            if len(word1) > len(word2):
                return False
            return True

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not compare(words[i], words[j]):
                    return False
        return True