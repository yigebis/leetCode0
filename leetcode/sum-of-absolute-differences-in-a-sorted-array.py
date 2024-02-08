class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre_sum = [nums[0]]
        result = []

        for i in range(1, len(nums)):
            pre_sum.append(pre_sum[-1] + nums[i])

        total_sum = pre_sum[-1]
        for i in range(len(nums)):
            right_sum = total_sum - pre_sum[i]
            left_sum = pre_sum[i] - nums[i]
            right_len = len(nums) - i - 1
            left_len = i

            result.append(right_sum - nums[i] * right_len + nums[i] * left_len - left_sum)

        return result


