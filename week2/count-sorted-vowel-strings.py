class Solution:
    def countVowelStrings(self, n: int) -> int:
        next_vowels = {
            'a' : ['a', 'e', 'i', 'o', 'u'],
            'e' : ['e', 'i', 'o', 'u'],
            'i' : ['i', 'o', 'u'],
            'o' : ['o', 'u'],
            'u' : ['u']
        }
        

        possibilities = [{'a' : -1, 'e' : -1, 'i' : -1, 'o' : -1, 'u' : -1} for i in range(n)]
        for vowel in next_vowels:
            possibilities[0][vowel] = 1

        def helper(n, vowel):
            if possibilities[n-1][vowel] != -1:
                return possibilities[n - 1][vowel]
            
            level_ans = 0
            for next_vowel in next_vowels[vowel]:
                level_ans += helper(n - 1, next_vowel)
            
            possibilities[n - 1][vowel] = level_ans
            
            return possibilities[n - 1][vowel]
        
        valids = 0
        for vowel in next_vowels:
            valids += helper(n, vowel)
        
        return valids