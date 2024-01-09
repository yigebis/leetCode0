class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # l = 0
        # r = len(s1) - 1
        # s1 = sorted(s1)
        # while r < len(s2):
        #     if s1 == sorted(s2[l:r+1]):
        #         return True
        #     r += 1
        #     l += 1
        # return False

        if len(s1) > len(s2):
            return False

        first_map, second_map = {}, {}
        l, r = 0, 0
        
        while r < len(s1):
            first_map[s1[r]] = 1 + first_map.get(s1[r], 0)
            second_map[s2[r]] = 1 + second_map.get(s2[r], 0)
            r += 1
        while r < len(s2):
            if first_map == second_map:
                return True
            if second_map[s2[l]] == 1:
                second_map.pop(s2[l])
            else:
                second_map[s2[l]] -= 1
            second_map[s2[r]] = 1 + second_map.get(s2[r], 0)
            l += 1
            r += 1
        if first_map == second_map:
            return True
        return False

        