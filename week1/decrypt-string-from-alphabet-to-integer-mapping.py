class Solution:
    def freqAlphabets(self, s: str) -> str:
        to_letter = {}
        # 1 -> ord(1) = 49
        # ord(a) = 97
        # chr(ord(number) + 48)
        i = len(s) - 1
        ans = ""
        for p in range(1,27):
            to_letter[str(p)] = chr(p + 96)
        while i >= 0:
            if s[i] == '#':
                ans += to_letter[s[i - 2] + s[i - 1]]
                i -= 2
            else:
                ans += to_letter[s[i]]
            i -= 1
        return ans[::-1]
