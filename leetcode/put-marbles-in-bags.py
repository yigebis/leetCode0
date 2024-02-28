class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1 or len(weights) == k:
            return 0
        arr = []
        for i in range(len(weights) - 1):
            arr.append(weights[i] + weights[i+1])
        
        maxs, mins = weights[0], weights[0]
        arr.sort()

        for i in range(k - 1):
            mins += arr[i]
            maxs += arr[len(arr) - i - 1]
        
        maxs += weights[len(weights) - 1]
        mins += weights[len(weights) - 1]
        return maxs - mins