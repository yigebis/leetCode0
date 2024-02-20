class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = 0
        stack = []

        for t in tokens:
            # print(stack)
            if t == '+' or t == '*' or t == '-':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val = eval(str(val2) + t + str(val1))
                stack.append(str(val))
            elif t == '/':
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                sign = 1
                if (val1 < 0 and val2 > 0) or (val1 > 0 and val2 < 0):
                    sign = -1
                val = (abs(val2) // abs(val1)) * sign
                stack.append(str(val))
            else:
                stack.append(t)
        val = int(stack.pop())
        return val
