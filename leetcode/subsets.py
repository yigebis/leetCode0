class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(l, start):
            ans.append(l.copy())
            if len(l) == len(nums):
                return
            for i in range(start, len(nums)):
                l.append(nums[i])
                backtrack(l, i + 1)
                l.pop()
        backtrack([], 0)
        return ans
                
