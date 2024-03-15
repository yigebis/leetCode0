class Solution:
    def possible(self, speed):
        hours = 0
        for pile in self.piles:
            hours += ceil(pile/speed)
            if hours > self.h:
                return False
        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        self.h = h
        l, r = 1, max(piles)
        min_speed = r

        while l <= r:
            mid = l + (r - l)//2
            if self.possible(mid):
                r = mid - 1
                min_speed = mid
            else:
                l = mid + 1
        
        return min_speed