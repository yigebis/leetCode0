class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        amounts = {5 : 0, 10 : 0, 20 : 0}
        for i in range(len(bills)):
            # determine the return
            returns = bills[i] - 5
            # greedily give the return
            if amounts[10] > 0 and returns >= 10:
                returns -= 10 
                amounts[10] -= 1
            if amounts[5] * 5 < returns:
                return False
            amounts[5] -= returns // 5

            amounts[bills[i]] += 1

        return True