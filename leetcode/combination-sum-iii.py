class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        valids = []

        def backtrack(l, start, total):
            if len(l) == k:
                if total == n:
                    valids.append(l.copy())
                return
            
            for i in range(start, 10):
                total += i
                l.append(i)
                backtrack(l, i + 1, total)
                total -= i
                l.pop()
        backtrack([], 1, 0)

        return valids