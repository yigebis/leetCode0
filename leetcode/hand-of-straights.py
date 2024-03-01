class Solution:
    def isNStraightHand(self, hand: List[int], group_size: int) -> bool:
        if len(hand) % group_size != 0:
            return False
        hand.sort()
        left = defaultdict(int)
        for num in hand:
            left[num] += 1
        for i in range(len(hand)):
            if left[hand[i]] == 0:
                continue
            next_num = hand[i] + 1
            for j in range(group_size - 1):
                if left[next_num] == 0:
                    return False
                left[next_num] -= 1
                next_num += 1
            left[hand[i]] -= 1
        
        return True