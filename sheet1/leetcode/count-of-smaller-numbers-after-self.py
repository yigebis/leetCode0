class Solution:
    def merge(self, left_half, right_half):
        l = r = 0
        arr = []
        temp = 0
        while l < len(left_half) and r < len(right_half):
            if self.nums[left_half[l]] <= self.nums[right_half[r]]:
                arr.append(left_half[l])
                self.right_min[left_half[l]] += temp
                l += 1
            else:
                arr.append(right_half[r])
                r += 1
                temp += 1
        while l < len(left_half):
            arr.append(left_half[l])
            self.right_min[left_half[l]] += temp
            l += 1
        while r < len(right_half):
            arr.append(right_half[r])
            r += 1
        return arr
    def mergeSort(self, l, r):
        arr = self.index
        if l == r:
            return [arr[l]]

        mid = l + (r-l)//2
        left_half = self.mergeSort(l, mid)
        right_half = self.mergeSort(mid + 1, r)

        return self.merge(left_half, right_half)
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.nums = nums
        self.index = [i for i in range(len(nums))]
        self.right_min = [0 for i in range(len(nums))]
        self.mergeSort(0, len(self.index) - 1)

        return self.right_min