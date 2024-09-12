# Problem: Find the Student that Will Replace the Chalk - https://leetcode.com/problems/find-the-student-that-will-replace-the-chalk/description/

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        chalk_replacer = -1
        pre_sum = [chalk[0]]

        for i in range(1, len(chalk)):
            pre_sum.append(chalk[i] + pre_sum[-1])
        
        total = pre_sum[-1]
        rem = k % total

        l, r = 0, len(pre_sum) - 1

        while l <= r:
            mid = l + (r - l)//2

            if pre_sum[mid] > rem:
                chalk_replacer = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return chalk_replacer

