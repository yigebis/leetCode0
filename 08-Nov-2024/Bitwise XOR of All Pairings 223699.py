# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = 0
        if not (len(nums1) & 1) and not (len(nums2) & 1):
            return 0

        if len(nums1) & 1:
            for num in nums2:
                xor ^= num
        
        if len(nums2) & 1:
            for num in nums1:
                xor ^= num
        

        
        
        return xor
