class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        seen=set()
        def right(row, col):
            while col<n:
                if mat[row][col]=='w'or mat[row][col]=='h'or  mat[row][col]=='b' or  mat[row][col]=='g':
                    break
                if mat[row][col]=='v':
                    mat[row][col]='b'
                else:
                    mat[row][col]='h'
                col+=1
        def left(row, col):
            while col>=0:
                if mat[row][col]=='w'or mat[row][col]=='h'or  mat[row][col]=='b' or  mat[row][col]=='g':
                    break
                if mat[row][col]=='v':
                    mat[row][col]='b'
                else:
                    mat[row][col]='h'
                col-=1
        def up(row, col):
            while row>=0:
                if mat[row][col]=='w'or mat[row][col]=='v'or  mat[row][col]=='b' or  mat[row][col]=='g':
                    break
                if mat[row][col]=='h':
                    mat[row][col]='b'
                else:
                    mat[row][col]='v'
                row-=1
        def down(row, col):
            while row<m:
                if mat[row][col]=='w'or mat[row][col]=='v'or  mat[row][col]=='b' or  mat[row][col]=='g':
                    break
                if mat[row][col]=='h':
                    mat[row][col]='b'
                else:
                    mat[row][col]='v'
                row+=1
            
        mat = [[0 for i in range(n)] for i in range(m)]

        for w in walls:
            mat[w[0]][w[1]]='w'

        for g in guards:
            row = g[0]
            col = g[1]
            right(row, col + 1)
            left(row, col - 1)
            up(row - 1, col)
            down(row + 1, col)
            mat[g[0]][g[1]]='g' 
        cnt=0
        for row in range(m):
            for col in range(n):
                if mat[row][col]==0:
                    cnt+=1
        return cnt