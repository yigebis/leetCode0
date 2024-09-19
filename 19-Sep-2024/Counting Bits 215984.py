# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for i in range(n+1)]

        for i in range(n+1):
            if i * 2 <= n:
                ans[i * 2] = ans[i]

            if i % 2 == 0 and i + 1 <= n:
                 ans[i + 1] = ans[i] + 1
        
        return ans