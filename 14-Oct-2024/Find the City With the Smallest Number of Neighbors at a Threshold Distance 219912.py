# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # floyd warshal algorithm
        shortest = [[inf for i in range(n)] for i in range(n)]

        for u, v, w in edges:
            shortest[u][v] = w
            shortest[v][u] = w
        
        for i in range(n):
            shortest[i][i] = 0
            

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    candidate = shortest[j][i] + shortest[k][i]
                    shortest[k][j] = min(shortest[k][j], candidate)
                    shortest[j][k] = shortest[k][j]
        
        min_reachables = n
        answer = -1

        for i in range(n):
            reachables = 0
            for j in range(n):
                if shortest[i][j] <= distanceThreshold:
                    reachables += 1
            reachables -= 1
            if reachables <= min_reachables:
                min_reachables = reachables
                answer = i
        
        return answer