class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        to_letter = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        letter_comb = []

        def backtrack(l, start):
            if l and len(l) == len(digits):
                letter_comb.append("".join(l.copy()))
                return
            for i in range(start, len(digits)):
                letters = to_letter[digits[i]]
                for j in range(len(letters)):
                    l.append(letters[j])
                    backtrack(l, i + 1)
                    l.pop()
        
        backtrack([], 0)
        return letter_comb
