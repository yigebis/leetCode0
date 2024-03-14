"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        solution = []
        for i in range(1, 1001):
            if customfunction.f(i, 1) > z or customfunction.f(i, 1000) < z:
                continue
            left, right = 1, 1000
            while left <= right:
                mid = left + (right - left)//2
                value = customfunction.f(i, mid)
                if value == z:
                    solution.append([i, mid])
                    break
                if value < z:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return solution