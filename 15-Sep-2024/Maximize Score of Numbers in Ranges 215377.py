# Problem: Maximize Score of Numbers in Ranges - https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:

        def check(diff):
            curr = start[0]
            for i in range(1, len(start)):
                nxt = curr + diff
                if nxt > start[i] + d:
                    return False
                curr = max(start[i], nxt)
                
            return True

        start.sort()

        l, r = 0, start[-1] + d - start[0]
        ans = 0

        while l <= r:
            mid = l + (r - l)//2
            if check(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return ans