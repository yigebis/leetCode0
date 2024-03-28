class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n != 1 and n % 2 == 0:
            n //= 2
        while n != 1 and n % 3 == 0:
            n //= 3
        while n != 1 and n % 5 == 0:
            n //= 5
        if n != 1:
            return False
        return True