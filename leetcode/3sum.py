class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2 2
        nums.sort()
        index = 0
        # three_sum = []
        exists = set()
        while index < len(nums) - 2:
            look_for = 0 - nums[index]
            l = index + 1
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == look_for:
                    exists.add((nums[index], nums[l], nums[r]))
                    r -= 1
                    l += 1
                elif nums[l] + nums[r] > look_for:
                    r -= 1
                else:
                    l += 1
            index += 1
        return list(exists)
                
