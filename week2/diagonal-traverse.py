class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        self.i = 0
        self.j = 0
        diagonals = []
        def top_right():
            while self.i >= 0 and self.j < len(mat[0]):
                if self.i < len(mat) and self.j >= 0:
                    diagonals.append(mat[self.i][self.j])
                self.i -= 1
                self.j += 1
            self.i += 1
            
        def bottom_left():
            while self.i < len(mat) and self.j >= 0:
                if self.i >= 0 and self.j < len(mat[0]):
                    diagonals.append(mat[self.i][self.j])
                self.i += 1
                self.j -= 1

            self.j += 1
        while len(diagonals) < len(mat) * len(mat[0]):
            top_right()
            bottom_left()
        return diagonals