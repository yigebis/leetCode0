class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        index = k
        arr_sum = max_sum
        while index < len(nums):
            arr_sum = arr_sum - nums[index - k] + nums[index]
            max_sum = max(max_sum, arr_sum)
            index += 1
        return max_sum/k 