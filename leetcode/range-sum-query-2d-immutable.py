class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre_sum_mat = matrix
        for i in range(1, len(self.pre_sum_mat)):
            self.pre_sum_mat[i][0] += self.pre_sum_mat[i-1][0]
        for j in range(1, len(self.pre_sum_mat[0])):
            self.pre_sum_mat[0][j] += self.pre_sum_mat[0][j-1]
        for i in range(1, len(self.pre_sum_mat)):
            for j in range(1, len(self.pre_sum_mat[0])):
                self.pre_sum_mat[i][j] = self.pre_sum_mat[i][j-1] + self.pre_sum_mat[i-1][j] - self.pre_sum_mat[i-1][j-1] + self.pre_sum_mat[i][j]
        print(self.pre_sum_mat)    

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 == 0 and col1 == 0:
            return self.pre_sum_mat[row2][col2]
        if row1 == 0:
            return self.pre_sum_mat[row2][col2] - self.pre_sum_mat[row2][col1-1]
        if col1 == 0:
            return self.pre_sum_mat[row2][col2] - self.pre_sum_mat[row1-1][col2]
        return self.pre_sum_mat[row2][col2] - self.pre_sum_mat[row2][col1-1] - self.pre_sum_mat[row1-1][col2] + self.pre_sum_mat[row1-1][col1-1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)