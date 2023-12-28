class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] < arr[0]:
            return False
        flag = ">"
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            if flag == ">":
                if arr[i] < arr[i-1]:
                    flag = "<"
            else:
                if arr[i] > arr[i-1]:
                    return False
        if flag == ">":
            return False
        return True