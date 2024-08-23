# Problem: Fraction Addition and Subtraction - https://leetcode.com/problems/fraction-addition-and-subtraction/

class Solution:
    def calc_res(self, curr, operand, oper):
        denominator = lcm(operand[1], curr[1])

        numerator1 = (denominator // curr[1]) * curr[0]
        numerator2 = (denominator // operand[1]) * operand[0]

        numerator = 0
        if oper == "+":
            numerator = numerator1 + numerator2
        else:
            numerator = numerator1 - numerator2
        
        return [numerator, denominator]
        
    def fractionAddition(self, exp: str) -> str:
        res = [0, 1]

        oper = "+"
        i = 0
        while i in range(len(exp)):
            if exp[i] == "+" or exp[i] == "-":
                oper = exp[i]
                i += 1
                continue
            
            numerator = 0
            while i < len(exp) and '0' <= exp[i] <= '9':
                    numerator *= 10
                    numerator += int(exp[i])
                    i += 1
            
            i += 1

            denominator = 0
            while i < len(exp) and '0' <= exp[i] <= '9':
                    denominator *= 10
                    denominator += int(exp[i])
                    i += 1
            operand = [numerator, denominator]
            # print(operand)
            prev_res = res
            res = self.calc_res(res, operand, oper)
            # print(operand, prev_res, res, oper)
        
        _gcd = gcd(res[0], res[1])
        if _gcd != 1:
            res[0] //= _gcd
            res[1] //= _gcd

        return str(res[0]) + "/" + str(res[1])
            
                