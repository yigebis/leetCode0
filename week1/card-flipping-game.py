class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        doubles = set()
        minimum = 1001

        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                doubles.add(fronts[i])
        fronts += backs

        for i in range(len(fronts)):
            if fronts[i] < minimum and fronts[i] not in doubles:
                minimum = fronts[i]
        if minimum == 1001:
            return 0
        return minimum