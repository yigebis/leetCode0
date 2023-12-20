class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        def swap(b, e):
            i = b
            while b < e:
                l[b], l[e] = l[e], l[b]
                b += 1
                e -= 1
        for i in range(0, len(l) - 1, 2*k):
            swap(i, min(i + k - 1, len(l) - 1))
        return "".join(l)
        