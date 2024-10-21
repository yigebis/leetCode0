# Problem: Maximum Width Ramp - https://leetcode.com/problems/maximum-width-ramp

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            nums[i] = (nums[i], i)
        
        nums.sort()

        min_idx, max_width = len(nums), 0
        for num, idx in nums:
            if idx < min_idx:
                min_idx = idx
            
            max_width = max(max_width, idx - min_idx)
        

        return max_width
