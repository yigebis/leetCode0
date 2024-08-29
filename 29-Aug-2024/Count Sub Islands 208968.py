# Problem: Count Sub Islands - https://leetcode.com/problems/count-sub-islands/

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        sub_islands = 0
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = set()

        def inbound(i, j):
            return 0 <= i < len(grid2) and 0 <= j < len(grid2[0])

        def dfs(start):
            status = True
            stack = [start]
            # path = [start]
            visited.add(start)
            while stack:
                x, y = stack.pop()
                if grid1[x][y] == 0:
                    status = False

                for d in directions:
                    new_x, new_y = x + d[0], y + d[1]
                    if inbound(new_x, new_y) and (new_x, new_y) not in visited and grid2[new_x][new_y] == 1:
                        stack.append((new_x, new_y))
                        visited.add((new_x, new_y))
                        # path.append((new_x, new_y))
                        
            if status:
                # print(path)
                return 1
            return 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and (i,j) not in visited:
                    sub_islands += dfs((i,j))

        return sub_islands