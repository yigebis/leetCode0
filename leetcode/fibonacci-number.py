class Solution:
    covered = {}
    def fib(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        if n in self.covered:
            return self.covered[n]
        
        self.covered[n] = self.fib(n-1) + self.fib(n-2)
        return self.covered[n]
        