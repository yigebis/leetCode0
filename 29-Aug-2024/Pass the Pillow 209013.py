# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        period = n - 1
        total_turns = time // period
        rem = time % period

        if total_turns & 1:
            return period - rem + 1
        else:
            return rem + 1