class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # 2 2 3 4
        # 
        valids = 0
        nums.sort()

        for i in range(len(nums) - 1, 1, -1):
            if nums[i] == 0:
                break
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] <= nums[i]:
                    l += 1
                else:
                    valids += r - l
                    r -= 1
            
        return valids
