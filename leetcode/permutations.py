class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(l):
            if len(l) == len(nums):
                ans.append(l.copy())
                return
            for i in nums:
                if i not in l:
                    l.append(i)
                    backtrack(l)
                    l.pop()

        backtrack([])
        return ans