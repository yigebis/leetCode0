# Problem: Convert 1D Array Into 2D Array - https://leetcode.com/problems/convert-1d-array-into-2d-array/

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        ind = 0
        mat = []
        for i in range(m):
            arr = []
            for j in range(n):
                arr.append(original[ind + j])
            ind += n
            mat.append(arr)
        
        return mat
        