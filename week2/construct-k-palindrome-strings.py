class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        count = defaultdict(int)
        ones = 0
        for ch in s:
            count[ch] += 1
        for c in count:
            if count[c] % 2 == 1:
                ones += 1
        if ones > k:
            return False
        return True