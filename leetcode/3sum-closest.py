class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        index = 0
        closest = nums[0] + nums[1] + nums[2]
        min_difference = abs(closest - target)
        while index < len(nums) - 2:
            l, r = index + 1, len(nums) - 1
            while l < r:
                three_sum = nums[l] + nums[r] + nums[index]
                if abs(three_sum - target) < min_difference:
                    min_difference = abs(three_sum - target)
                    closest = three_sum
                if closest  == target:
                    return closest
                if three_sum < target:
                    l += 1
                else:
                    r -= 1
            index += 1

        return closest
            