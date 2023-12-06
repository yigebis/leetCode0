class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        for i in range(1, n+1):
            total_money += ((i % 7) + (i // 7))

        
        return total_money + 6 * (n // 7)