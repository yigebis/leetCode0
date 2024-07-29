# Problem: Sort the Jumbled Numbers - https://leetcode.com/problems/sort-the-jumbled-numbers/

class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        
        def to_map(x):
            if x == 0:
                return mapping[0]

            mapped = 0
            mul = 1

            while x:
                last = x % 10
                x //= 10
                mapped += mapping[last] * mul
                mul *= 10
            
            return mapped


        nums.sort(key = lambda x : to_map(x))

        return nums