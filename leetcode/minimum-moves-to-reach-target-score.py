class Solution:
    def minMoves(self, target: int, max_doubles: int) -> int:
        min_moves = 0
        num = target

        while num > 1:
            if max_doubles == 0:
                return min_moves + num - 1
            min_moves += num % 2
            num //= 2
            max_doubles -= 1
            min_moves += 1
        return min_moves
        