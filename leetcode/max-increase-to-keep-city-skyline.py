class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        max_inc = 0

        max_in_row, max_in_col = defaultdict(int), defaultdict(int)
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                max_in_row[i] = max(max_in_row[i], grid[i][j])
                max_in_col[j] = max(max_in_col[j], grid[i][j])
        
        for i in range(rows):
            for j in range(cols):
                max_inc += min(max_in_row[i], max_in_col[j]) - grid[i][j]
        
        return max_inc

