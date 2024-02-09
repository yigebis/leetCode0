class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        complete, incomplete = 0, 0
        total_subarrays = (len(nums) * (len(nums) + 1))//2
        seen = set()
        for i in range(len(nums)):
            seen.add(nums[i])
        max_size = len(seen)
        freq = {}
        l = 0
        for r in range(len(nums)):
            freq[nums[r]] = 1 + freq.get(nums[r], 0)
            while len(freq) == max_size and l < len(nums):
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    freq.pop(nums[l])
                l += 1
            incomplete += r - l + 1
        
        complete = total_subarrays - incomplete
        return complete
