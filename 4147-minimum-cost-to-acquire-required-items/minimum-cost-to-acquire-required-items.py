class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        min_cost, max_cost = min(cost1, cost2), max(cost1, cost2)
        if costBoth <= min_cost:
            return costBoth * max(need1, need2)

        if min_cost + max_cost <= costBoth:
            return cost1 * need1 + cost2 * need2
        
        # if costBoth <= max_cost:
        if need1 < need2:
            return costBoth * need1 + min(costBoth, cost2) * (need2 - need1)
        
        return min(costBoth, cost1) * (need1 - need2) + costBoth * need2
        
        # return cost1 * need1 + cost2 * need2