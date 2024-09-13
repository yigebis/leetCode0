# Problem: Meaningless Operations - https://codeforces.com/problemset/problem/1110/C

from math import gcd, sqrt, ceil
q = int(input())

for i in range(q):
    n = int(input())
    b = bin(n)[2:]
    
    req = 2**len(b) - 1
    if req != n:
        print(req)
    else:
        ans = 1
        if len(b) & 1:
            for i in range(2, ceil(sqrt(req)) + 1):
                if req % i == 0:
                    ans = req//i
                    break
            print(ans)
        else:
            binary = "0b"
            for _ in range(len(b)//2):
                binary += "0"
                binary += "1"
            ans = int(binary, base=0)
            print(ans)