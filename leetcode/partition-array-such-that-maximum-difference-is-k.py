class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        subsequences = 0
        nums.sort()
        l = 0

        for r in range(len(nums)):
            if nums[r] - nums[l] > k:
                subsequences += 1
                l = r

        subsequences += 1
        return subsequences