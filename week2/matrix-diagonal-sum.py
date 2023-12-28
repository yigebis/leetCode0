class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j == len(mat) - 1 or i == j:
                    total += mat[i][j]
        
        return total



