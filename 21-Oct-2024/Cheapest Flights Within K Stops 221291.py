# Problem: Cheapest Flights Within K Stops - https://leetcode.com/problems/cheapest-flights-within-k-stops/

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        curr = [inf for i in range(n)]
        prev = [inf for i in range(n)]
        curr[src], prev[src] = 0, 0

        for i in range(k + 1):
            change = False
            for fro, to, price in flights:
                curr_cost = prev[fro] + price
                if curr[to] > curr_cost:
                    curr[to] = curr_cost
                    change = True
            
            if not change:
                break
            prev = curr[:]
        
        return curr[dst] if curr[dst] != inf else -1