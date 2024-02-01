class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        count = 1
        res = 1
        type_to_index = {fruits[0] : 0}

        for r in range(1, len(fruits)):
            if fruits[r] in type_to_index:
                type_to_index[fruits[r]] = r
                res = max(res, r - l + 1)
            elif count < 2:
                type_to_index[fruits[r]] = r
                res = max(res, r - l + 1)
                count += 1
            else:
                minimum = 100000
                popped = 0
                for i in type_to_index:
                    if type_to_index[i] < minimum:
                        minimum = type_to_index[i]
                        popped = i
                l = minimum + 1
                type_to_index.pop(popped)
                type_to_index[fruits[r]] = r
        return res