class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        def call_prev(k):
            if k == 0:
                return 0
            prev = call_prev(k//2)
            if k%2 == 0:
                return prev
            if prev == 1:
                return 0
            return 1
        return call_prev(k-1)