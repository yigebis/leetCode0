class Solution:
    def minimumSteps(self, s: str) -> int:
        min_steps = 0
        r = len(s) - 1
        while s[r] == '1' and r >= 0:
            r -= 1
        if r == -1:
            return 0
        l = r
        while s[l] == '0' and l >= 0:
            l -= 1
        
        while l >= 0:
            if s[l] == '1':
                min_steps += r - l
                r -= 1
            l -= 1
        
        return min_steps
            
            


        