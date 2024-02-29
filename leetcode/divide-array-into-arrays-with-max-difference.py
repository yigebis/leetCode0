class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        valids = []
        nums.sort()
        l = 0
        for r in range(2, len(nums), 3):
            if nums[r] - nums[l] <= k:
                valids.append(nums[l : r + 1])
                l = r + 1
            else:
                valids = []
                break
        
        return valids