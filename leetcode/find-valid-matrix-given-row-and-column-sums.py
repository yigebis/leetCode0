class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        zero_count = 0
        grid = [[0 for i in range(len(colSum))] for i in range(len(rowSum))]


        curr_sum = sum(rowSum)
        
        for i in range(len(grid)):
            grid[i][0] = rowSum[i]
        
        for i in range(len(colSum)):
            if curr_sum == colSum[i]:
                break
            diff = curr_sum - colSum[i]
            curr_sum = 0
            for j in range(len(rowSum)):
                if diff == 0:
                    break
                decr = min(grid[j][i], diff)
                grid[j][i] -= decr
                grid[j][i+1] += decr
                diff -= decr
                curr_sum += decr
        return grid

            
