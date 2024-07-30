# Problem: Number of Pairs Satisfying Inequality - https://leetcode.com/problems/number-of-pairs-satisfying-inequality/

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        diff_arr = [nums1[i] - nums2[i] for i in range(len(nums1))]
        ans = 0

        def merge(a, b):
            nonlocal ans
            i, j = 0, 0

            while i < len(a) and j < len(b):
                if a[i] <= b[j] + diff:
                    ans += len(b) - j
                    # print(a[i], b[j], a, b, len(b) - j)
                # if a[i] <= b[j]:
                #     c.append(a[i])
                #     ans += len(b) - j - 1
                    i += 1
                else:
                    j += 1
            
            # while i < len(a):
            #     c.append(a[i])
            #     i += 1
            # while j < len(b):
            #     c.append(b[j])
            #     j += 1
            return sorted(a + b)
            
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr)//2
            left_part = merge_sort(arr[0:mid])
            right_part = merge_sort(arr[mid:])

            return merge(left_part, right_part)
        
        merge_sort(diff_arr)


        return ans

            
