class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = '/'

        directory = path.split('/')
        stack = []
        for d in directory:
            if d == '' or d == '.':
                continue
            if d == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(d)
        canonical += '/'.join(stack)
        return canonical

