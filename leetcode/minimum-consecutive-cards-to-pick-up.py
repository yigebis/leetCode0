class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # 5 6 3 2 4 3 4
        #         l   r
        seen = set()
        l = 0
        min_len = len(cards) + 1
        for r in range(len(cards)):
            while cards[r] in seen:
                min_len = min(min_len, r - l + 1)
                seen.remove(cards[l])
                l += 1
            seen.add(cards[r])
        
        if min_len == len(cards) + 1:
            return -1
        return min_len

