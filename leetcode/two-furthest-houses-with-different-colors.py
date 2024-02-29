class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        for i in range(len(colors) - 1, 0, -1):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)
                break
        
        for i in range(len(colors) - 1):
            if colors[i] != colors[len(colors) - 1]:
                max_dist = max(max_dist, len(colors) - 1 - i)
                break
        
        return max_dist