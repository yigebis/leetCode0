class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def maxPower(n):
            i = 0
            while 3**i <= n:
                i += 1
            return i - 1
        prev_power = -1
        while n > 0:
            power = maxPower(n)
            if power == prev_power:
                return False
            n -= 3**power
            prev_power = power
        return True
