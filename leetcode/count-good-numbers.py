class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd_place = n//2
        even_place = n - odd_place

        return (pow(5, even_place, 1000000007) * pow(4, odd_place, 1000000007)) % (1000000007)