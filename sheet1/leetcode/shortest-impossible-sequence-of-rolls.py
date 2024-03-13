class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        found = 0
        uniques = set()
        for i in range(len(rolls)):
            uniques.add(rolls[i])
            if len(uniques) == k:
                found += 1
                uniques = set()
        
        return found + 1