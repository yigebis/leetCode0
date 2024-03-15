class Solution:
    def possible(self, rad):
        l, r = 0, 0
        achieved = 0
        while l < len(self.houses) and r < len(self.heaters):
            if self.houses[l] > achieved and self.houses[l] < self.heaters[r] - rad:
                return False
            curr_left = self.heaters[r] - rad
            curr_right = self.heaters[r] + rad
            while l < len(self.houses) and self.houses[l] <= curr_right and self.houses[l] >= curr_left:
                l += 1
            achieved = curr_right
            r += 1
        while l < len(self.houses) and self.houses[l] <= achieved:
            l += 1
        if l < len(self.houses):
            return False
        return True 
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        self.houses, self.heaters = houses, heaters
        left, right = 0, 1000000000
        min_rad = right

        while left <= right:
            mid = left + (right - left) // 2
            if self.possible(mid):
                right = mid - 1
                min_rad = mid
            else:
                left = mid + 1
        
        return min_rad
