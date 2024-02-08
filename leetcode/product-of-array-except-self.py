class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1 2 3 4 5
        # 1 2 6 24 120
        # 120 120 60 20 5
        # 1 * 2 * 3 * 6 * 4 = 24
        # 1 * 2 * 3 = 6
        left_pro, right_pro = [], [nums[-1] for i in range(len(nums))]
        left_pro.append(nums[0])
        pro_except_self = []

        for i in range(1, len(nums)):
            left_pro.append(nums[i] * left_pro[-1])
        for i in range(len(nums) - 2, -1, -1):
            right_pro[i] = right_pro[i+1] * nums[i]

        pro_except_self.append(right_pro[1])
        for i in range(1, len(nums) - 1):
            pro_except_self.append(right_pro[i+1] * left_pro[i-1])
        pro_except_self.append(left_pro[-2])

        return pro_except_self
