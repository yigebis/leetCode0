class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        char_set = set()
        for ch in s:
            char_set.add(ch)
        for i in range(len(s)):
            ch = s[i]
            if ch.lower() in char_set and ch.upper() in char_set:
                continue
            left = self.longestNiceSubstring(s[0:i])
            right = self.longestNiceSubstring(s[i+1:])
            if len(left) >= len(right):
                return left
            else:
                return right
        return s