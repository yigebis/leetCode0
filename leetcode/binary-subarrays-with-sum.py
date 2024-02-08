class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def helper(goal):
            l, r = 0, 0
            sum = 0
            res = 0
            while r < len(nums):
                sum += nums[r]
                while sum > goal and l <= r:
                    sum -= nums[l]
                    l += 1
                res += r - l + 1
                r += 1
            return res
        return helper(goal) - helper(goal - 1)