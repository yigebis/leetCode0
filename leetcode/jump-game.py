class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i in range(len(nums) - 1):
            if nums[i] == 0 and max_idx == i:
                return False
            max_idx = max(max_idx, i + nums[i])
        
        return True