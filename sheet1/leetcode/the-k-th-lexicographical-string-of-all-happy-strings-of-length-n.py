class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = ""
        count = 0
        def backtrack(l):
            nonlocal count, ans

            if len(l) == n:
                print(l)
                count += 1
                if count == k:
                    ans = "".join(l[:])
                return
            
            for ch in "abc":
                if count == k:
                    return
                if not l:
                    l.append(ch)
                elif l[-1] == ch:
                    continue
                else:
                    l.append(ch)
                backtrack(l)
                l.pop()
        backtrack([])

        return ans

                