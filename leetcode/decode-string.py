class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = len(s) - 1
        while i >= 0:
            if s[i] >= '0' and s[i] <= '9':
                num_str = ""
                while i >= 0 and s[i] >= '0' and s[i] <= '9':
                    num_str = s[i] + num_str
                    i -= 1
                num = int(num_str)
                curr = ""
                stack.pop()
                while stack[-1] != ']':
                    curr += stack.pop()
                curr *= num
                stack.pop()
                for j in range(len(curr) - 1,-1,-1):
                    stack.append(curr[j])
            else:
                stack.append(s[i])
                i -= 1
        to_str = "".join(stack)
            
        return to_str[-1::-1]