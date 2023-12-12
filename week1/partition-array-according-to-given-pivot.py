class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # trivial one
        arr1, arr2 = [], []
        count = 0

        for num in nums:
            if num < pivot:
                arr1.append(num)
            elif num > pivot:
                arr2.append(num)
            else:
                count += 1
        
        for i in range(count):
            arr1.append(pivot)
        
        return arr1 + arr2
        