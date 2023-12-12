class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        set_of_ranges = set()

        for i in ranges:
            l = []
            for j in range(i[0], i[1] + 1):
                l.append(j)
            set_of_ranges.update(l)

        # print(set_of_ranges)
        for i in range(left, right + 1):
            if i not in set_of_ranges:
                return False
        
        return True