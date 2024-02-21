class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1/self.myPow(x, -n)
        if x == 0:
            return float(x)
        if n == 0:
            return 1
        if n % 2 == 0:
            return self.myPow(x * x, n//2)
        return x * self.myPow(x, n-1)