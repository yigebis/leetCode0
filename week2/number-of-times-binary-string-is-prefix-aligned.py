class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maximum = 0
        count = 0

        for i in range(len(flips)):
            maximum = max(maximum, flips[i])
            if maximum == i + 1:
                count += 1
        
        return count
                
