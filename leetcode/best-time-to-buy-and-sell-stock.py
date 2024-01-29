class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = len(prices) - 1
        max_profit = 0
        max_price = 0

        while i >= 0:
            if prices[i] > max_price:
                max_price = prices[i]
            else:
                max_profit = max(max_profit, max_price - prices[i])
            i -= 1
        
        return max_profit
