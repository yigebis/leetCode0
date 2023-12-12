class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l = 0
        shuffled = []
        while l < n:
            shuffled.append(nums[l])
            shuffled.append(nums[l + n])
            l += 1
        return shuffled