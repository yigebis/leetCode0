class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        next_greater = {}
        stack = []
        # i = len(nums2) - 1
        # while i >= 0:
        #     while stack and stack[-1] < nums2[i]:
        #         stack.pop()
        #     if not stack:
        #         next_greater[nums2[i]] = -1
        #     else:
        #         next_greater[nums2[i]] = stack[-1]
        #     stack.append(nums2[i])
        #     i -= 1
        # for j in range(len(nums1)):
        #     nums1[j] = next_greater[nums1[j]]
        # return nums1

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                next_greater[stack[-1]] = nums2[i]
                stack.pop()
            stack.append(nums2[i])
        while stack:
            next_greater[stack.pop()] = -1
        for i in range(len(nums1)):
            ans.append(next_greater[nums1[i]])
        
        return ans
        
        