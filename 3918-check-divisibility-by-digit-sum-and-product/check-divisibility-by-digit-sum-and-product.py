class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def find_digits(num):
            digits = []
            while num:
                digits.append(num % 10)
                num //= 10
            return digits
        
        digits = find_digits(n)
        dig_sum, dig_prod = 0, 1
        for digit in digits:
            dig_sum += digit
            dig_prod *= digit
        
        return n % (dig_sum + dig_prod) == 0
