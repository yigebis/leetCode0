class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        dir = 1
        curr = 1
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and dir == 1:
                curr += 1
            elif nums[i] < nums[i-1] and dir == 0:
                curr += 1
            elif nums[i] == nums[i-1]:
                curr = 1
            else:
                dir ^= 1
                curr = 2
            ans = max(ans, curr)
        
        return ans