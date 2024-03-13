class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        mid = 0
        left_right = []
        
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                left_right = [mid, mid]
                break
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        if l > r:
            return [-1, -1]
        
        # find leftmost
        l , r = 0, left_right[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid - 1
            else:
                l = mid + 1
        left_right[0] = l 
        
        # find rightmost
        l , r = left_right[0], len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid + 1
            else:
                r = mid - 1
        left_right[1] = r

        return left_right