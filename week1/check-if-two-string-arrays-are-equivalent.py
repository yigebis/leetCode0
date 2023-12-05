class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        to_string1 = to_string2 = ""
        
        for sub1 in word1:
            to_string1 += sub1
        
        for sub2 in word2:
            to_string2 += sub2
        
        return to_string1 == to_string2