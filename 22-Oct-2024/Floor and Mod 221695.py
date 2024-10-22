# Problem: Floor and Mod - https://codeforces.com/problemset/problem/1485/C

import sys, threading
from math import isqrt
# from collections import defaultdict

input = lambda : sys.stdin.readline().strip()


def read_arr():
    return list(map(int, input().split()))
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
def read_mult():
    return map(int, input().split())

def first_xor(n):
    if n % 4 == 0:
        return n
    if n % 4 == 1:
        return 1
    if n % 4 == 2:
        return n + 1
    return 0

t = int(input())
for _ in range(t):
    x, y = read_mult()
    ans = 0
    
    # the remainder and the quotient, which is a single number, should be less than or equal to sqrt(x)
    # proof
    # let k be the remainder
    # a = kb + k
    # kb + k = a ; and a <= x
    # kb + k <= x
    # k < b
    # kk + k <= x
    # k^2 <= x - k
    # k^2 <= x
    # k <= sqrt(x)
    for k in range(1, isqrt(x) + 1):
        # how many b's can we assign to the equation a = kb + k = k(b + 1)
        # lower bound for b is k + 1
        lower = k + 1
        # upper bound for b is y
        # watch out for another upper bound, b shouldn't also make a > x
        # so let a = x, then x = k(b + 1) -> b = x/k - 1
        # if we increase b more than this, a > x
        # so the upper bound is the minimum of the 2 upper bounds
        upper = min(x//k - 1, y)
        # so now the answer is the number of integers from lower to upper
        # which is upper - lower + 1
        # but this number can be negative (upper < lower), so make it 0 in that case
        curr = max(0, upper - lower + 1)
        ans += curr
    
    print(ans)