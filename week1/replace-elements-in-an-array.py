class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            dict[nums[i]] = i
        for l in operations:
            nums[dict[l[0]]] = l[1]
            # dict.pop(l[0])
            dict[l[1]] = dict[l[0]]
        return nums 