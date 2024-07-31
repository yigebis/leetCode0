# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = [set() for i in range(n)]
        graph = [[] for i in range(n)]
        parent_count = [0 for i in range(n)]
        # edges.sort()

        for edge in edges:
            graph[edge[0]].append(edge[1])
            parent_count[edge[1]] += 1
        
        queue = deque()
        for i in range(n):
            if parent_count[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                ancestors[child].update(ancestors[node])
                ancestors[child].add(node)
                parent_count[child] -= 1
                if parent_count[child] == 0:
                    queue.append(child)

        for i in range(len(ancestors)):
            ancestors[i] = sorted(list(ancestors[i]))
            
        return ancestors        
