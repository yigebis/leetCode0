class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = 0, 1
        rearranged = [0] * len(nums)

        for num in nums:
            if num > 0:
                rearranged[p] = num
                p += 2
            else:
                rearranged[n] = num
                n += 2
        
        return rearranged