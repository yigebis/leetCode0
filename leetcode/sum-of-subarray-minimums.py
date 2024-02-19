class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        '''
        Let's approach this question using a monotonic stack
        What about thinking of the span to the left and to the right upto which
        a number is the minimum?
        eg. 3, 1, 2, 4, 1
        2 can be the minimum for 1 left subarray ([2]) and 2 right subarrays ([2], [2,4])
        so 2 can be the minimum for 2 * 1  = 2 subarrays.
        If we do the same for all and multiply the numbers by their total (left * right) spans
        and add them, don't we get the total?
        
        How do we do that? we use monotonic stack of indices and values (but monotonicity is by their values)
        eg. 3, 1, 2, 4, 1
        stack = [(-1, 0)]  //populating the stack with a -1 index with value 0
        is 3 > 0? yes so the left span of subarrays where 3 is minimum is 
        from -1 (not inclusive) upto 0 (inclusive). so 0 - -1 = 1 subarray
        stack = [(-1, 0), (0, 3)]
        is 1 > 3? No so we pop the top element and we record 2 things
        '''
        total = 0
        stack = [(-1, 0), (0, arr[0])]
        left_span = {0 : 1}
        right_span = {len(arr) : 0}
        

        for i in range(1, len(arr)):
            while arr[i] <= stack[-1][1]:
                right_span[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            left_span[i] = i - stack[-1][0]
            stack.append((i, arr[i]))
        while stack:
            right_span[stack[-1][0]] = len(arr) - stack[-1][0]
            # print(stack[-1])
            stack.pop()
        # print(left_span)
        # print(right_span)
        for i in range(len(arr)):
            total += arr[i] * (left_span[i] * right_span[i])
        
        return total % (1000000007)