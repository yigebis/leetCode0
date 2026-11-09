class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = Counter("balloon")
        count = Counter(text)
        min_freq = len(text)

        for ch in balloon_count:
            freq = count[ch] // balloon_count[ch]
            min_freq = min(min_freq, freq)
        
        return min_freq
