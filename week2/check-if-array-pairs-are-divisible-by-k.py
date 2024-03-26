class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mods = defaultdict(int)
        for num in arr:
            mod = num % k
            # print(mods, mod)
            need = 0
            if mod == 0:
                need = 0
            else:
                need = k - mod
            if need in mods:
                mods[need] -= 1
                if mods[need] == 0:
                    del mods[need]
            else:
                mods[mod] += 1
        
        if not mods:
            return True
        
        return False