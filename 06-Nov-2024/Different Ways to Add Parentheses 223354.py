# Problem: Different Ways to Add Parentheses - https://leetcode.com/problems/different-ways-to-add-parentheses/

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def combine(left, right, oper):
            comb = []
            
            for lnum in left:
                for rnum in right:
                    if oper == "+":
                        comb.append(lnum + rnum)
                    elif oper == "-":
                        comb.append(lnum - rnum)
                    else:
                        comb.append(lnum * rnum)
            
            return comb

        memo = {}
        def generate_answers(l, r):
            if r - l <= 1:
                return [int(expression[l:r+1])]
            
            if (l, r) in memo:
                return memo[(l, r)]

            curr_answers = []
            
            for i in range(l, r + 1):
                if expression[i] == "+" or expression[i] == "-" or expression[i] == "*":
                    left_results = generate_answers(l, i - 1)
                    right_results = generate_answers(i + 1, r)

                    curr_answers += combine(left_results, right_results, expression[i])
            
            memo[(l, r)] = curr_answers
            return curr_answers
        
        return generate_answers(0, len(expression) - 1)