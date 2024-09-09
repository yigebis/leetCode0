# Problem: Find Missing Observations - https://leetcode.com/problems/find-missing-observations/

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m_sum = sum(rolls)
        m = len(rolls)
        rem_sum = (n + m) * mean - m_sum
        arr = []

        max_avg = ceil(rem_sum / n)
        dist_avg = rem_sum // n

        if max_avg > 6 or dist_avg < 1:
            return arr
        
        for i in range(n):
            curr_assigned = min(rem_sum, dist_avg)
            arr.append(curr_assigned)
            rem_sum -= curr_assigned
        
        # print(arr)
        for i in range(rem_sum):
            arr[i] += 1

        return arr



