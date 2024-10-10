# Problem: Minimum Deletions to Make String Balanced - https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        ans = len(s)
        total_a = s.count("a")
        pre_a, pre_b = 0, 0

        for ch in s:
            suf_a = total_a - pre_a
            suf_a -= 1 if ch == "a" else 0
            ans = min(ans, pre_b + suf_a)

            if ch == "b":
                pre_b += 1
            else:
                pre_a += 1
        
        return ans