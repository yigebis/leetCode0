# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        answer = [-1 for i in range(len(queries))]
        pre_xor = [arr[0]]

        for i in range(1, len(arr)):
            num = arr[i]
            pre_xor.append(pre_xor[-1] ^ num)
        
        for i in range(len(queries)):
            l, r = queries[i]
            if l == 0:
                ans = pre_xor[r]
            else:
                ans = pre_xor[r] ^ pre_xor[l-1]

            answer[i] = ans

        return answer