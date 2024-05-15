class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        max_val = [-1 for i in range(len(arr))]

        def helper(start):
            if start >= len(arr):
                return 0
            
            if max_val[start] != -1:
                return max_val[start]
            
            partition_max = 0
            curr_max = arr[start]

            offset = start + k
            for i in range(start, min(offset, len(arr))):
                curr_max = max(curr_max, arr[i])
                taken = curr_max * (i - start + 1) + helper(i + 1)
                partition_max = max(taken, partition_max)
            
            max_val[start] = partition_max
            return partition_max
        
        return helper(0)
