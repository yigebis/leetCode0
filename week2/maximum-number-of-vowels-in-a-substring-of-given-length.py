class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        max_vowels = 0
        vowels = {'a','e','i','o','u'}
        l = 0
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_vowels = count
        for r in range(k,len(s)):
            if s[l] in vowels:
                count -= 1
            if s[r] in vowels:
                count += 1
            max_vowels = max(max_vowels, count)
            l += 1
        return max_vowels
