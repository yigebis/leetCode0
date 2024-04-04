class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = 0
        visited = set()
        def dfs(city):
            stack = [city]
            visited.add(city)

            while stack:
                node = stack.pop()
                for i in range(len(isConnected)):
                    if i not in visited and isConnected[node][i] == 1:
                        stack.append(i)
                        visited.add(i)
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1
        
        return provinces