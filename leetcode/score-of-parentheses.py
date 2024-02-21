class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ')' and stack[-1] == '(':
                stack.pop()
                stack.append(1)
            else:
                val = stack.pop()
                stack.pop()  #removing the opening parenthesis
                stack.append(2 * val)

            if stack[-1] != '(' and stack[-2] != '(':
                stack.append(stack.pop() + stack.pop())
        
        return stack.pop()
            
