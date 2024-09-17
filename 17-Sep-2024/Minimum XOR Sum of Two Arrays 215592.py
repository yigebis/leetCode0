# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}

        def dfs(ind, chosen):
            if ind >= len(nums1):
                return 0
            
            if (ind, chosen) in memo:
                return memo[(ind, chosen)]

            min_ans = inf

            for i in range(len(nums2)):
                shift = 1 << i
                if chosen & shift:
                    continue

                chosen |= shift
                curr_ans = (nums1[ind] ^ nums2[i]) + dfs(ind + 1, chosen)
                min_ans = min(min_ans, curr_ans)

                chosen ^= shift

            memo[(ind, chosen)] = min_ans
            return min_ans
        
        return dfs(0,0)
