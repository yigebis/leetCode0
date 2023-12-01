class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map = {}
        counter = 0
        for i in nums:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        for i in hash_map:
            counter += (hash_map[i] * (hash_map[i] - 1))//2 
        return counter