class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        l, r = 0, 0
        while l < len(name) and r < len(typed):
            if name[l] != typed[r]:
                return False
            l_count, r_count = 0, 0
            char = typed[r]

            while l < len(name) and name[l] == char:
                l_count += 1
                l += 1
            while r < len(typed) and typed[r] == char:
                r_count += 1
                r += 1
            if l_count > r_count:
                return False
        if r < len(typed) or l < len(name):
            return False
        return True