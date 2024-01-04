class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        square = set()
        for i in range(9):
            for j in range(9):
                    ch = board[i][j]
                    if ch != ".":
                        if ch in row[i] or ch in col[j] or (i//3, j//3, ch) in square:
                            print(square)
                            print(row)
                            print(col)
                            return False
                        else:
                            row[i].add(ch)
                            col[j].add(ch)
                            square.add((i//3,j//3,ch))
        return True
        
                

                
