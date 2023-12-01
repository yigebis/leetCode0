class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        i = len(s) - 1
        ans = roman_to_int[s[i]]
        i -= 1
        while i >= 0:
            if roman_to_int[s[i]] >= roman_to_int[s[i+1]]:
                ans += roman_to_int[s[i]]
            else:
                ans -= roman_to_int[s[i]]
            i -= 1
        return ans