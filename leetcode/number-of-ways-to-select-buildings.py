class Solution:
    def numberOfWays(self, s: str) -> int:
        # 00110111
        # 55433210 -ones
        # 21110000 -zeros
        valids = 0
        right_ones, right_zeros = [0 for i in range(len(s))], [0 for i in range(len(s))]
        left_zeros, left_ones = 0, 0
        for i in range(len(s) - 2, -1, -1):
            if s[i+1] == '0':
                right_zeros[i] = right_zeros[i+1] + 1
                right_ones[i] = right_ones[i+1]
            else:
                right_ones[i] = right_ones[i+1] + 1
                right_zeros[i] = right_zeros[i+1]
        for i in range(len(s)):
            if s[i] == '0':
                valids += left_ones * right_ones[i]
                left_zeros += 1
            else:
                valids += left_zeros * right_zeros[i]
                left_ones += 1
        
        return valids
        
