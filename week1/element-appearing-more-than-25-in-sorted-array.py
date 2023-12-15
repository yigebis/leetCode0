class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freq = defaultdict(int)
        max_observed = -1
        max_freq = 0
        for i in arr:
            freq[i] += 1
            if freq[i] > max_freq:
                max_freq = freq[i]
                max_observed = i
                
        return max_observed
        