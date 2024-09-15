# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        masks = [1,0,0,0,2,0,0,0,4,0,0,0,0,0,8,0,0,0,0,0,16,0,0,0,0,0]
        curr_mask = 0
        ans = 0

        prev_masks = {0 : -1}

        for i in range(len(s)):
            curr_mask ^= masks[ord(s[i]) - 97]
            if curr_mask in prev_masks:
                ans = max(ans, i - prev_masks[curr_mask])
            else:
                prev_masks[curr_mask] = i
        
        return ans
        