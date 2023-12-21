class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        indices = {}
        count = 0
        for i in range(len(nums)):
            if nums[i] in indices:
                for index in indices[nums[i]]:
                    if (index * i) % k == 0:
                        count += 1
                indices[nums[i]].append(i)
            else:
                indices[nums[i]] = [i]
                
        return count