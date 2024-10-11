# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for i in range(n)]
        probable =  [0 for i in range(n)]
        probable[start] = 1

        for i in range(len(edges)):
            a, b = edges[i]
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])
        
        heap = [(-1, start)]
        visited = set()

        while heap:
            prob, node = heappop(heap)
            prob *= -1
            visited.add(node)

            for neigh, neigh_prob in graph[node]:
                if neigh in visited:
                    continue

                curr_prob = probable[node] * neigh_prob
                if probable[neigh] < curr_prob:
                    probable[neigh] = curr_prob
                    heappush(heap, (-curr_prob, neigh))
        
        return probable[end]
