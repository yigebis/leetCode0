class Solution:
    def balancedString(self, s: str) -> int:
        # QWERQWQQ
        #        l
        #        r
        # Q : 3 W : 2 E : 1 R : 1
        # res = 2
        # QWER
        #  l
        #  r
        # Q : 1 W :  E : 1 R : 1

        l, r = 0, 0
        res = 100001
        letter_count = {"Q" : 0, "W" : 0, "R" : 0, "E" : 0}
        for ch in s:
            letter_count[ch] += 1
        if letter_count["Q"] == letter_count["W"] == letter_count["E"] == len(s)//4:
            return 0
        while r < len(s):
            letter_count[s[r]] -= 1
            while max(letter_count.values()) <= len(s)//4 and l <= r:
                letter_count[s[l]] += 1
                res = min(res, r - l + 1)
                l += 1
            r += 1
        return res
        