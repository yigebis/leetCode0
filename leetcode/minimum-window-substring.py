class Solution:
    def compare(self, dict1, dict2):
        for ch in dict1:
            if dict1[ch] > dict2.get(ch, 0):
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count_in_t = {}
        count_in_s = {}
        min_substring = ""
        min_length = 100000
        for i in range(len(t)):
            count_in_t[t[i]] = 1 + count_in_t.get(t[i], 0)
        
        for i in range(len(s)):
            count_in_s[s[i]] = 1 + count_in_s.get(s[i], 0)
            while (self.compare(count_in_t, count_in_s)):
                if i - l + 1 < min_length:
                    min_length = i - l + 1
                    min_substring = s[l:i+1]
                count_in_s[s[l]] -= 1
                l += 1
        return min_substring
                


