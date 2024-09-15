# Problem: Longest Subarray With Maximum Bitwise AND - https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_size = 0
        max_num = max(nums)
        l, r = 0, 0

        while l in range(len(nums)):
            if nums[l] == max_num:
                r = l
                while r < len(nums) and nums[r] == max_num:
                    r += 1
                max_size = max(max_size, r - l)
                l = r
            else:
                l += 1

        return max_size
