class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        total = 0
        res = 0
        for i in range(len(grid) - 3 + 1):
            for j in range(len(grid[0]) - 3 + 1):
                total += grid[i][j] + grid[i][j+1] + grid[i][j+2]
                total += grid[i+1][j+1]
                total += grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                res = max(res, total)
                total = 0
        return res