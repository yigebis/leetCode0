class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if (len(p) > len(s)): return []
        pCount = {}
        sCount = {}
        res = []
        for i in range(len(p)):
            if(p[i] in pCount):
                pCount[p[i]] += 1
            else:
                pCount[p[i]] = 1
            if (s[i] in sCount):
                sCount[s[i]] += 1
            else:
                sCount[s[i]] = 1
        if sCount == pCount:
            res.append(0)
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1
            if sCount == pCount:
                res.append(l)
        return res

        
        