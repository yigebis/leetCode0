class Solution:
    def maxScore(self, s: str) -> int:
        left_zeros = [1 if s[0] == '0' else 0]
        right_ones = [0 for i in range(len(s))]
        right_ones[-1] = 1 if s[-1] == '1' else 0
        max_score = 0

        for i in range(1, len(s)):
            if s[i] == '0':
                left_zeros.append(left_zeros[-1] + 1)
            else:
                left_zeros.append(left_zeros[-1])
        for i in range(len(s) - 2, -1, -1):
            if s[i] == '1':
                right_ones[i] = right_ones[i+1] + 1
            else:
                right_ones[i] = right_ones[i+1]
        for i in range(len(s) - 1):
            max_score = max(max_score, left_zeros[i] + right_ones[i+1])
        
        return max_score