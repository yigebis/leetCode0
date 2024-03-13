# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 0, n
        while l <= r:
            mid = l + (r - l)//2
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
# 1 10 - 5
# 1 4 - 2
# 2 4 - 3