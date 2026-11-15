class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        ans = 0
        MOD = 10**9 + 7
        curr_odd, next_odd = -1, -1
        dp = [0]*len(arr)

        for i in range(len(arr) - 1, -1, -1):
            num = arr[i]
            if num & 1:
                if curr_odd != -1:
                    diff = curr_odd - i
                    dp[i] += diff
                    if next_odd != -1:
                        dp[i] += dp[next_odd]
                    next_odd = curr_odd
                    curr_odd = i
                else:
                    dp[i] = len(arr) - i
                    curr_odd = i
            
            else:
                if curr_odd != -1:
                    dp[i] = dp[curr_odd]
            
            ans += dp[i]
            ans %= MOD
        
        # print(dp)
        return ans
        

