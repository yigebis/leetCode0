class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        max_total = 0
        requested = [0 for i in range(len(nums) + 1)]
        for start, end in requests:
            requested[start] += 1
            requested[end + 1] -= 1
        for i in range(1, len(requested) - 1):
            requested[i] += requested[i-1]
        requested.pop()

        nums.sort()
        requested.sort()

        for i in range(len(nums)):
            max_total += nums[i] * requested[i]

        return max_total % 1000000007