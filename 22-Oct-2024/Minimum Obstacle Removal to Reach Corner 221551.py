# Problem: Minimum Obstacle Removal to Reach Corner - https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m

        heap = [(0, 0, 0)]
        visited = [[0 for i in range(m)] for i in range(n)]
        distance = [[inf for i in range(m)] for i in range(n)]
        distance[0][0] = 0

        while heap:
            dist, x, y = heappop(heap)
            visited[x][y] = 1

            for dx, dy in directions:
                newx, newy = x + dx, y + dy
                if not inbound(newx, newy) or visited[newx][newy]:
                    continue

                curr_dist = distance[x][y] + grid[newx][newy]

                if curr_dist < distance[newx][newy]:
                    distance[newx][newy] = curr_dist
                    heappush(heap, (curr_dist, newx, newy))
        
        return distance[n-1][m-1]
                
                
            