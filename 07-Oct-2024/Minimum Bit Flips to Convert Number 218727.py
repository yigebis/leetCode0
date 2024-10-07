# Problem: Minimum Bit Flips to Convert Number - https://leetcode.com/problems/minimum-bit-flips-to-convert-number/

class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        bit_start = bin(start)[2:]
        bit_goal = bin(goal)[2:]

        if len(bit_start) > len(bit_goal):
            bit_goal = "0"*(len(bit_start) - len(bit_goal)) + bit_goal
        else:
            bit_start = "0"*(len(bit_goal) - len(bit_start)) + bit_start
        
        for i in range(len(bit_start)):
            if bit_start[i] != bit_goal[i]:
                ans += 1
        
        return ans