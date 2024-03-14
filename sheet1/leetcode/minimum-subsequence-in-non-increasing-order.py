class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        max_seq = []
        total = sum(nums)
        running = 0
        nums.sort(reverse=True)
        for i in range(len(nums)):
            max_seq.append(nums[i])
            running += nums[i]
            if running > total - running:
                return max_seq
                
        return max_seq
