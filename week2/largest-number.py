class comparator(str):
    def __lt__(a, b):
        # if str(a) + str(b) > str(b) + str(a):
        #     return a
        # return b
        return a + b > b + a
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key = comparator)
        if nums[0] == "0":
            return "0"
        return "".join(nums)