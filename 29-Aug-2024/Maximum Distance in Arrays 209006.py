# Problem: Maximum Distance in Arrays - https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_diff = 0
        if len(arrays) == 1:
            return 0
        
        first_minimum, second_minimum = inf, inf
        
        for array in arrays:
            arr_minimum = array[0]
            if arr_minimum < first_minimum:
                second_minimum = first_minimum
                first_minimum = arr_minimum
            elif arr_minimum < second_minimum:
                second_minimum = arr_minimum


        for i in range(len(arrays)):
            curr_max = arrays[i][-1]
            if first_minimum != arrays[i][0]:
                max_diff = max(max_diff, curr_max - first_minimum)
            else:
                max_diff = max(max_diff, curr_max - second_minimum)
        
        return max_diff