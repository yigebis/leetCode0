class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        subarray = set()
        score = 0
        max_score = 0
        l = 0

        for r in range(len(nums)):
            while nums[r] in subarray:
                subarray.remove(nums[l])
                score -= nums[l]
                l += 1
            score += nums[r]
            subarray.add(nums[r])
            max_score = max(max_score, score)
        
        return max_score