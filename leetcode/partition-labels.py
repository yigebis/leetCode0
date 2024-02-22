class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        ans = []
        size = 0
        for i in range (len(s)):
            lastIndex[s[i]] = i
        end = lastIndex[s[0]]
        for i in range(len(s)):
            end = max(end, lastIndex[s[i]])
            size += 1
            if end == i:
                ans.append(size)
                size = 0
        return ans
