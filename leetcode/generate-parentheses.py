class Solution:
    close, open = 0, 0
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        s = ""
        def backtrack(s):
            if self.open == self.close and self.open == n:
                ans.append(s)
                return
            if self.open < n:
                s += '('
                self.open += 1
                backtrack(s)
                s = s[:-1]
                self.open -= 1
            if self.close < self.open:
                s += ')'
                self.close += 1
                backtrack(s)
                s = s[:-1]
                self.close -= 1
        backtrack("")
        return ans


            