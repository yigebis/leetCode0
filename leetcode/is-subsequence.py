class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r  = 0, 0
        while l < len(s):
            while r < len(t):
                if t[r] == s[l]:
                    l += 1
                    r += 1
                    break
                r += 1
            if r == len(t):
                break
        if l < len(s):
            return False
        return True

            

        