class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        ans = 0
        for num1 in arr1:
            less = False
            for num2 in arr2:
                if abs(num2 - num1) <= d:
                    less = True
            if not less:
                ans += 1
        
        return ans