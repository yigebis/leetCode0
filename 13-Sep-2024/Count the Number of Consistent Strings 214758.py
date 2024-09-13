# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        allowed_set = set()

        for ch in allowed:
            allowed_set.add(ch)

        for s in words:
            stat = True
            for ch in s:
                if ch not in allowed_set:
                    stat = False
                    break
            ans += 1 if stat else 0
        
        return ans
