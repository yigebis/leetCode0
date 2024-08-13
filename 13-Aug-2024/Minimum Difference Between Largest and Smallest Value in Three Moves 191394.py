# Problem: Minimum Difference Between Largest and Smallest Value in Three Moves - https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        diff = inf
        nums.sort()
        
        for left in range(4):
            right = left + len(nums) - 3 - 1
            diff = min(diff, nums[right] - nums[left])
        
        return diff