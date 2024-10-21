# Problem: Design Graph With Shortest Path Calculator - https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for i in range(n)]

        for src, dst, cost in edges:
            self.graph[src].append([dst, cost])
        

    def addEdge(self, edge: List[int]) -> None:
        src, dst, cost = edge[0], edge[1], edge[2]
        self.graph[src].append([dst, cost])

    def shortestPath(self, src: int, dst: int) -> int:
        n = self.n
        min_cost = [inf for i in range(n)]
        min_cost[src] = 0
        visited = set()

        heap = [(0, src)]

        while heap:
            node_cost, node = heappop(heap)

            if node in visited:
                continue
            if node == dst:
                return min_cost[node]

            for neigh, neigh_cost in self.graph[node]:
                if neigh not in visited:
                    min_cost[neigh] = min(min_cost[neigh], node_cost + neigh_cost)
                    heappush(heap, (min_cost[neigh], neigh))

            visited.add(node)
        
        if min_cost[dst] == inf:
            return -1
        return min_cost[dst]

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)