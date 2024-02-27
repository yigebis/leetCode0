class Solution:
    # def custom_converter(arr):
        
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        def backtrack(l, start):
            ans.append("".join(l))
            if start == len(s):
                return
            for i in range(start, len(s)):
                prev = l[i]
                if l[i] >= 'A' and l[i] <= 'Z':
                    l[i] = l[i].lower()
                elif l[i] >= 'a' and l[i] <= 'z':
                    l[i] = l[i].upper()
                else:
                    continue
                backtrack(l, i + 1)
                l[i] = prev
        # print()
        # l = list(s)
        # ans.append("".join(l))
        backtrack(list(s), 0)
        return ans