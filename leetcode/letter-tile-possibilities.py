class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        ans = 0
        seen_index = set()

        def backtrack(l):
            # print(l)
            nonlocal ans
            if l != []:
                ans += 1
            if len(l) == len(tiles):
                return
            traversed = set()
            for i in range(len(tiles)):
                if tiles[i] in traversed or i in seen_index:
                    continue
                l.append(tiles[i])
                seen_index.add(i)
                backtrack(l)
                l.pop()
                seen_index.remove(i)
                traversed.add(tiles[i])
        backtrack([])
        return ans
