class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = {
            '{': '}',
            '[' : ']',
            '(' : ')'
        }
        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if stack and closing[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True