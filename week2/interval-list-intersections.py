class Solution:
    def intervalIntersection(self, first: List[List[int]], second: List[List[int]]) -> List[List[int]]:
        ans = []
        f, s = 0, 0
        while f < len(first) and s < len(second):
            if (first[f][0] >= second[s][0] and first[f][0] <= second[s][1]) or (second[s][0] >= first[f][0] and second[s][0] <= first[f][1]):
                ans.append([max(first[f][0], second[s][0]), min(first[f][1], second[s][1])])
            if first[f][1] > second[s][1]:
                s += 1
            else:
                f += 1
        return ans