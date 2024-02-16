class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for p in s:
            if p == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(p)
                
        return len(stack)