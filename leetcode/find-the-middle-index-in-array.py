class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = [nums[0]]
        total = nums[0]

        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])
            total += nums[i]
        
        for i in range(len(nums)):
            left_sum = pre_sum[i] - nums[i]
            right_sum = total - pre_sum[i]
            if left_sum == right_sum:
                return i
        
        return -1

