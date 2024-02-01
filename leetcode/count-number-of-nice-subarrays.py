class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        odds = 0
        nices = 0
        min_idx, max_idx = 0, len(nums)

        while r < len(nums):
            if nums[r] % 2:
                odds += 1
                if odds == 1:
                    min_idx = r
                if odds == k:
                    max_idx = r
                if odds > k:
                    nices += (min_idx - l + 1) * (r - max_idx)
                    l = min_idx + 1
                    odds -= 1
                    max_idx = r
                    for i in range(l, r + 1):
                        if nums[i] % 2:
                            min_idx = i
                            break
            r += 1
        nices += (min_idx - l + 1) * (r - max_idx)
        return nices
