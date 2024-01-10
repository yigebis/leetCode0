class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count, min_conversions = 0, 0
        l = 0
        for r in range(k):
            if blocks[r] == 'W':
                count += 1
        min_conversions = count
        for r in range(k,len(blocks)):
            if blocks[r] == 'W':
                count += 1
            if blocks[l] == 'W':
                count -= 1
            l += 1
            min_conversions = min(min_conversions, count)
        
        return min_conversions