class Solution:
    def printVertically(self, s: str) -> List[str]:
        splitted = s.split()
        ans = []
        index = 0
        # ["How", "are", "you"]
        # 
        max_size = 0
        for i in splitted:
            max_size = max(max_size, len(i))
        for n in range(max_size):
            new = ""
            temp = ""
            for i in range(len(splitted)):
                if index >= len(splitted[i]):
                    temp += " "
                else:
                    new += temp
                    new += splitted[i][index]
                    temp = ""
            index += 1
            ans.append(new)
        return ans