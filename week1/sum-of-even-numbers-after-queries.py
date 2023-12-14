class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # 1 2 3 4 evensum = 6
        # 2 2 3 4 even sum = 8
        # 2 -1 3 4 evensum = 6
        # -4 -1 3 4 evensum = 2
        # -4 -1 3 6 evensum = 4
        # we have the even sum of the array
        # traverse each query.
        # if the num at index is even and val is even, add val to evensum
        # elif the num at index is even and val is odd, subtract num from evensum
        # elif the num at index is odd and val is odd, add val + num to evensum
        # at each iteration change num by num + val and update the answer by evensum

        even_sum = 0
        answer = []

        for num in nums:
            if num % 2 == 0:
                even_sum += num

        for query in queries:
            if query[0] % 2 == 0 and nums[query[1]] % 2 == 0:
                even_sum += query[0]
            elif query[0] % 2 and nums[query[1]] % 2 == 0:
                even_sum -= nums[query[1]]
            elif query[0] % 2 and nums[query[1]] % 2:
                even_sum += nums[query[1]] + query[0]
            nums[query[1]] += query[0]
            answer.append(even_sum)
        
        return answer