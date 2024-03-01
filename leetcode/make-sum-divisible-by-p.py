class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        if total % p == 0:
            return 0
        rem = total % p
        running = 0
        min_dist = len(nums)
        pos = {0 : -1}

        for i in range(len(nums)):
            running = (running + nums[i]) % p
            new_rem = (running - rem) % p
            if new_rem in pos:
                min_dist = min(min_dist, i - pos[new_rem])
            pos[running] = i
        
        if min_dist == len(nums):
            return -1
        return min_dist

            