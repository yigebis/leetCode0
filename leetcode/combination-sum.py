class Solution:
    c = 0
    sum = 0
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(l, start):
            if self.sum == target:
                self.c += 1
                ans.append(l.copy())
            # if start == len(candidates):
            if self.sum > target:
                return
            for i in range(start, len(candidates)):
                self.sum += candidates[i]
                l.append(candidates[i])
                backtrack(l, i)
                self.sum -= candidates[i]
                l.pop()
        backtrack([], 0)
        return ans