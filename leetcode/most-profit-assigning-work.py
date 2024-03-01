class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_profit = 0

        for i in range(len(profit)):
            profit[i] = (profit[i], i)
        profit.sort()
        worker.sort()

        p, w = len(profit) - 1, len(worker) - 1
        while p >= 0 and w >= 0:
            if difficulty[profit[p][1]] <= worker[w]:
                max_profit += profit[p][0]
                w -= 1
            else:
                p -= 1
        
        return max_profit