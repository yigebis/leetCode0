class Solution:
    def minDeletions(self, s: str) -> int:
        # aaabbccddeeffgg
        dels = 0
        freq = [0 for i in range(26)]
        for ch in s:
            freq[ord(ch) - 97] += 1

        freq.sort(reverse=True)
        for i in range(1, 26):
            if freq[i] < freq[i-1]:
                continue
            else:
                if freq[i-1] == 0:
                    dels += freq[i]
                    freq[i] = 0
                else:
                    new = freq[i-1] - 1
                    dels += freq[i] - new
                    freq[i] = new

        return dels
