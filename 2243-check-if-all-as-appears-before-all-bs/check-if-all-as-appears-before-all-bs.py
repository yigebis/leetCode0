class Solution:
    def checkString(self, s: str) -> bool:
        b_found = False
        for ch in s:
            if ch == 'b':
                b_found = True
            elif b_found:
                return False
        
        return True
