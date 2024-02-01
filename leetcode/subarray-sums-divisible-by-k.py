class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        modulus = []
        modulus.append(nums[0])
        hash_map = {0 : 1}
        for i in range(1, len(nums)):
            modulus.append(modulus[i - 1] + nums[i])
        for i in range(len(nums)):
            modulus[i] %= k
            if modulus[i] in hash_map:
                ans += hash_map[modulus[i]]
                hash_map[modulus[i]] += 1
            else:
                hash_map[modulus[i]] = 1
        return ans
        # 4 9 9 7 4 5
        # 4 4 4 2 4 0


