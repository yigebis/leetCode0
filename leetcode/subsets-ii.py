class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        def backtrack(start, l):
            if l != []:
                subsets.append(l.copy())
            if start == len(nums):
                return
            traversed = set()
            for i in range(start, len(nums)):
                if nums[i] in traversed:
                    continue
                l.append(nums[i])
                backtrack(i + 1, l)
                l.pop()
                traversed.add(nums[i])
        backtrack(0, [])
        return subsets