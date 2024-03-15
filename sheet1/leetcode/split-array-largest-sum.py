class Solution:
    # 23 1 29 13
    def possible(self, value):
        arr = self.nums
        curr = 1
        running = 0
        for num in arr:
            running += num
            if running > value:
                running = num
                curr += 1
            if curr > self.k:
                return False
                
        return True
    def splitArray(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.k = k
        l, r = max(nums), sum(nums)
        smallest = r

        while l <= r:
            mid = l + (r - l)//2
            if self.possible(mid):
                r = mid - 1
                smallest = mid
            else:
                l = mid + 1
        
        return smallest