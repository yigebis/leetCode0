class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        complement = 0
        for i in range(len(nums)):
            dict[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict and dict[complement] != i:
                return [i, dict[complement]]
        return []