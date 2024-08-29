# Problem: Ugly Number II - https://leetcode.com/problems/ugly-number-ii/

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly_numbers = [1]
        two_candidate, three_candidate, five_candidate = 0, 0, 0

        while len(ugly_numbers) < n:
            by_two = ugly_numbers[two_candidate] * 2
            by_three = ugly_numbers[three_candidate] * 3
            by_five = ugly_numbers[five_candidate] * 5

            next_ugly = min(by_two, by_three, by_five)

            if by_two == next_ugly:
                two_candidate += 1
            elif by_three == next_ugly:
                three_candidate += 1
            else:
                five_candidate += 1
            
            if next_ugly != ugly_numbers[-1]:
                ugly_numbers.append(next_ugly)
        
        # print(ugly_numbers)
        return ugly_numbers[n - 1]

        