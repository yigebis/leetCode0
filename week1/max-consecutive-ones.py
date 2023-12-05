class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        res = 0
        for num in nums:
            if num == 1:
                counter += 1
            else:
                res = max(res, counter)
                counter = 0
        res = max(res, counter)
        return res