class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        seen = set()
        def backtrack(r, c, i):
            if i == (len(word)):
                return True
            if (r >= R or r < 0 or c < 0 or c >= C or word[i] != board[r][c] or (r,c) in seen):
                return False
            seen.add((r,c))
            result = backtrack(r + 1, c, i + 1) or backtrack(r - 1, c, i + 1) or backtrack(r, c + 1, i + 1) or backtrack(r, c - 1, i + 1)
            seen.remove((r,c))
            return result
        for i in range(R):
            for j in range(C):
                if(backtrack(i, j, 0)):
                    return True
        return False