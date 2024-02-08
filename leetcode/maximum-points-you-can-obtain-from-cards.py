class Solution:
    def maxScore(self, card_points: List[int], k: int) -> int:
        # 1 9 3 4 5 8
        if k == len(card_points):
            return sum(card_points)
        max_score = 0
        l, r = 0, len(card_points) - k - 1
        total = sum(card_points)
        sub_sum = sum(card_points[l : r + 1])

        while r < len(card_points):
            max_score = max(max_score, total - sub_sum)
            r += 1
            if r == len(card_points):
                break
            sub_sum += card_points[r] - card_points[l]
            l += 1
        return max_score

