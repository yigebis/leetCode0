class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return 0
        
        nums.sort()

        # option 1: replace first two
        diff1 = nums[-1] - nums[2]

        # option 2: replace last two
        diff2 = nums[-3] - nums[0]

        # option 3: replace one from each side
        diff3 = nums[-2] - nums[1]

        return min(diff1, diff2, diff3)