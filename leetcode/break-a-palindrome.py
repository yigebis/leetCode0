class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""

        arr = list(palindrome)
        ind = 0
        while ind < len(palindrome)//2 and palindrome[ind] == 'a':
            ind += 1
        if ind < len(palindrome)//2:
            arr[ind] = 'a'
        else:
            arr[len(arr) - 1] = 'b'
        
        return "".join(arr)