class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        running = 0
        avg = 0
        max_val = 0

        for i in range(len(nums)):
            running += nums[i]
            avg = ceil(running/(i + 1))
            max_val = max(max_val, avg)

        return max_val