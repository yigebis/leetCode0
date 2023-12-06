class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        can_be_maximum = []

        for candy in candies:
            if extraCandies + candy >= max_candy:
                can_be_maximum.append(True)
            else:
                can_be_maximum.append(False)
        
        return can_be_maximum