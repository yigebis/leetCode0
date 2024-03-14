class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        fulls = 0
        surplus = additionalRocks

        n = len(capacity)
        need = [capacity[i] - rocks[i] for i in range(n)]
        need.sort()
        for i in range(n):
            surplus -= need[i]
            if surplus < 0:
                break
            fulls += 1
        
        return fulls
