class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        actual_sum = sum(nums)
        assumed_sum = (len(nums) * (len(nums) + 1))//2

        return assumed_sum - actual_sum
