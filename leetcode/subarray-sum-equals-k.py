class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        preSumCount = {0 : 1}
        sum = 0
        count = 0
        for i in range (len(nums)):
            sum += nums[i]
            if (sum - k) in preSumCount:
                count += preSumCount[sum - k]
               # preSumCount[sum - k] = 0
            preSumCount[sum] = 1 + preSumCount.get(sum, 0)
            
        return count