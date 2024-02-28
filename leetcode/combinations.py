class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(start, l):
            if len(l) == k:
                ans.append(l.copy())
                return
            for i in range(start, n + 1):
                l.append(i)
                backtrack(i + 1, l)
                l.pop()

        backtrack(1, [])
        return ans

# 1 2 3 4
# 