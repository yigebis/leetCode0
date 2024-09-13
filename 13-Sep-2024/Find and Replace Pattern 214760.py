# Problem: Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        matches = []
        for word in words:
            mapping1, mapping2 = {}, {}
            stat = True
            for i in range(len(word)):
                if word[i] in mapping1 and mapping1[word[i]] != pattern[i]:
                    stat = False
                    break
                if pattern[i] in mapping2 and mapping2[pattern[i]] != word[i]:
                    stat = False
                    break
                mapping1[word[i]] = pattern[i]
                mapping2[pattern[i]] = word[i]
            
            if stat:
                matches.append(word)

        return matches 