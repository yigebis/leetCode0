class Solution:
    def minFlips(self, target: str) -> int:
        min_flips = 0
        turn = '0'

        for ch in target:
            if ch == '1' and turn == '0':
                min_flips += 1
                turn = '1'
            elif ch == '0' and turn == '1':
                min_flips += 1
                turn = '0'
        
        return min_flips

