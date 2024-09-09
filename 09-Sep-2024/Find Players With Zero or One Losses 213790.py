# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loses = {}
        seen = set()
        no_defeat = []
        one_defeat = []

        for i in matches:
            loses[i[1]] = 1 + loses.get(i[1], 0)
            seen.add(i[0])
            seen.add(i[1])
        for i in seen:
            if i not in loses:
                no_defeat.append(i)
            elif loses[i] == 1:
                one_defeat.append(i)
        no_defeat.sort()
        one_defeat.sort()

        return [no_defeat, one_defeat]

        