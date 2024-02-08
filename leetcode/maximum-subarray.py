class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_sum = 0
        pre_sum = [nums[0]]
        left_min = [0]
        for i in range(1,len(nums)):
            pre_sum.append(nums[i] + pre_sum[-1])
        for i in range(1,len(nums)):
            left_min.append(min(pre_sum[i-1], left_min[i-1]))
        
        max_sum = pre_sum[0] - left_min[0]
        for i in range(1,len(nums)):
            max_sum = max(max_sum, pre_sum[i] - left_min[i])
        # print(left_min, pre_sum)
        return max_sum

        # 5 9 8 15 23
        # 0 
