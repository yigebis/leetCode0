# Problem: Fedor and New Game - https://codeforces.com/contest/467/problem/B

import sys, threading

input = lambda : sys.stdin.readline().strip()


def read_arr():
    return list(map(int, input().split()))
def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()
def read_mult():
    return map(int, input().split())

n, m, k = read_mult()
players = []
for _ in range(m + 1):
    players.append(int(input()))
    
target = players[-1]
ans = 0

for p in range(m):
    curr = players[p]
    diff = 0
    for i in range(32):
        shift = 1 << i
        tar_bit, curr_bit = target & shift, curr & shift
        
        if (tar_bit and not curr_bit) or (not tar_bit and curr_bit):
            diff += 1
    
    if diff <= k:
        ans += 1

print(ans)