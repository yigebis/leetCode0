class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l, r = 0, 0
        s.sort()
        g.sort()

        ans = 0

        while l < len(g) and r < len(s) :
            while r < len(s) and g[l] > s[r]:
                r += 1
            if r < len(s) and g[l] <= s[r]:
                ans += 1
                l += 1
                r += 1
        return ans
