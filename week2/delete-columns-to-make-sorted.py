class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0
        for i in range(len(strs[0])):
            cmp = ""
            for j in range(len(strs)):
                if strs[j][i] < cmp:
                    count += 1
                    break
                cmp = strs[j][i]
        return count