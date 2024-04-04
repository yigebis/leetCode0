class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        great_letter = letters[0]
        l, r = 0, len(letters) - 1

        while l <= r:
            mid = l + (r - l)//2
            if letters[mid] > target:
                great_letter = letters[mid]
                r = mid - 1
            else:
                l = mid + 1
        
        return great_letter