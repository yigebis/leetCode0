class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        max_len = 0

        for ch in s:
            count[ch] = 1 + count.get(ch, 0)
        for c in count:
            max_len += count[c]//2
        
        max_len *= 2
        if max_len < len(s):
            max_len += 1
        return max_len
            
        
        