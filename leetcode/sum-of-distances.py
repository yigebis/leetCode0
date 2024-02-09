class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        left_to_right = [0 for i in range(len(nums))]
        right_to_left = [0 for i in range(len(nums))]
        arr = [0 for i in range(len(nums))]

        # the tuples indicate that the nearest nums[i] has been seen in the left direction
        # at i index and has a count c
        # and also the nearest nums[i] from right to left direction has been seen at index
        # i and has a count c
        l_r, r_l = {nums[0] : (0, 1)}, {nums[len(nums) - 1] : (len(nums) - 1, 1)}
        for i in range(1, len(nums)):
            count = 0
            if nums[i] in l_r:
                near_idx = l_r[nums[i]][0]
                count = l_r[nums[i]][1]
                val = left_to_right[near_idx]
                dist = i - near_idx
                left_to_right[i] = val + dist*count
            l_r[nums[i]] = (i, count + 1)  
        for i in range(len(nums) - 2, -1, -1):
            count = 0
            if nums[i] in r_l:
                near_idx = r_l[nums[i]][0]
                count = r_l[nums[i]][1]
                val = right_to_left[near_idx]
                dist = near_idx - i
                right_to_left[i] = val + dist * count
            r_l[nums[i]] = (i, count + 1)
            
        for i in range(len(nums)):
            arr[i] = left_to_right[i] + right_to_left[i]

        return arr 