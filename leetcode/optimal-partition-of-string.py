class Solution:
    def partitionString(self, s: str) -> int:
        min_subs = 1
        count = defaultdict(int)

        for r in range(len(s)):
            if count[s[r]] > 0:
                min_subs += 1
                count.clear()
            count[s[r]] += 1
        
        return min_subs