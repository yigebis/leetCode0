class Solution:
    def best(self, hash_map: dict):
        maximum = 0
        for i in hash_map:
            maximum = max(maximum, hash_map[i])
        return maximum
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        hash_map = {}
        for r in range(len(s)):
            hash_map[s[r]] = 1 + hash_map.get(s[r], 0)
            if (r - l + 1) - self.best(hash_map) <= k:
                res = max(res, r - l + 1)
            else: 
                hash_map[s[l]] -= 1
                l += 1
        return res
            
