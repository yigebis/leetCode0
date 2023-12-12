class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # first sort the array
        # start from the last index and check for validity of three lengths at last
        # iterate until the 3rd index, i = 2
        # if valid return the length of the three numbers
        # else 
        # 
        # return 0
        nums.sort()
        index = len(nums) - 1

        def check_validity(a, b, c):
            return a + b > c and b + c > a and a + c > b

        while index > 1:
            if check_validity(nums[index], nums[index-1], nums[index-2]):
                return nums[index] + nums[index-1] + nums[index-2]
            index -= 1
        return 0
# a + b > c
# a + c > b
# b + c > a