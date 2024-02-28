class Solution:
    sum = 0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def backtrack(l, start):
            if self.sum == target:
                ans.append(l.copy())
                return
            if self.sum > target:
                return
            covered = set()
            for i in range(start, len(candidates)):
                if (candidates[i] > target or candidates[i] in covered):
                    continue
                l.append(candidates[i])
                self.sum += candidates[i]
                backtrack(l, i + 1)
                l.pop()
                self.sum -= candidates[i]
                covered.add(candidates[i])
        backtrack([], 0)
        return ans