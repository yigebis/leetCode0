class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 1 _ 3 4 _ _
        # add 2
        # 1 1 3

        # 1 (2) (4) 5 10
        # 1, (2), 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 

        # 1 2 4 8 16 32
        # 1,2,3,4,5,6,7,8,

        # 1 2 4 5 10
        # 22
        # arr = []
        max_last = 0
        added = 0

        for i in range(len(nums)):
            while nums[i] > max_last + 1:
                if max_last >= n:
                    return added
                max_last += max_last + 1
                added += 1
            max_last += nums[i]
        while n > max_last:
            max_last += max_last + 1
            added += 1
        return added

        