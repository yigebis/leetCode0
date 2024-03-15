class Solution:
    def to_answer(self, ans, l):
        new_l = []
        for i in range(len(l)):
            new_l.append("".join(l[i]))
        ans.append(new_l)
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 2:
            return []
        ans = []
        rows, cols, d1, d2 = set(), set(), set(), set()

        def backtrack(l, count, start_row, start_col):
            if count == n:
                # print(l)
                self.to_answer(ans, l)
                return
            for i in range(start_row, n):
                for j in range(start_col, n):
                    if i in rows or j in cols or j - i in d1 or i + j in d2:
                        continue
                    if i > 0 and i - 1 not in rows:
                        return
                    l[i][j] = 'Q'
                    
                    rows.add(i)
                    cols.add(j)
                    d1.add(j - i)
                    d2.add(i + j)
                    count += 1
                    backtrack(l, count, i + 1, 0)
                    count -= 1
                    l[i][j] = '.'
                    rows.remove(i)
                    cols.remove(j)
                    d1.remove(j - i)
                    d2.remove(i + j)
        l = [['.' for i in range(n)] for i in range(n)]
        backtrack(l, 0, 0, 0)

        return ans
