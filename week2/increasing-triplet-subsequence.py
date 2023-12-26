class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        pre_min, post_max = [nums[0] for i in range(len(nums))], [nums[len(nums) - 1] for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            pre_min[i] = min(pre_min[i-1], nums[i - 1])
        for i in range(len(nums) - 2, -1, -1):
            post_max[i] = max(post_max[i+1], nums[i+1])
        for i in range(len(nums)):
            if pre_min[i] < nums[i] < post_max[i]:
                return True
        return False
