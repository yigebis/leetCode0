class Solution:
    def smallestNumber(self, num: int) -> int:    
        if num >= 0:
            s = list(str(num))
            s.sort() 
            swapped = 0
            for i in range(len(s)):
                if s[i] != "0":
                    swapped = i
                    break
            s[0], s[swapped] = s[swapped], s[0]
            return int("".join(s))

        else:
            s = list(str(num)[1:])
            s.sort(reverse=True)
            return int("".join(s))*-1

        
            

