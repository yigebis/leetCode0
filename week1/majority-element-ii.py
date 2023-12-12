class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # using dictionary
        count = {}
        more_than_floor = []
        floor = len(nums)//3
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        
        for c in count:
            if count[c] > floor:
                more_than_floor.append(c)
        
        return more_than_floor