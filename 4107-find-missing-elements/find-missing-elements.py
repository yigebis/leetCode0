class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        st = set(nums)
        lost = []
        for num in range(min(nums) + 1, max(nums)):
            if num not in st:
                lost.append(num)
        
        return lost