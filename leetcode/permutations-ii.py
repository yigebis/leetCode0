class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        in_seen = set()

        def backtrack(start, l):
            if len(l) == len(nums):
                ans.append(l.copy())
                # in_seen.clear()
                return
            # if nums[start] in seen:
            #     return
            seen = set()
            for i in range(start, len(nums)):
                if i in in_seen or nums[i] in seen:
                    continue
                print(l)    
                l.append(nums[i])
                in_seen.add(i)
                backtrack(0, l)
                l.pop()
                in_seen.remove(i)
                seen.add(nums[i])
        backtrack(0,[])
        return ans