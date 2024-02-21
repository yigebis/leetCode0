class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        result = [0 for i in range(len(deck))]
        
        deck.sort()
        ind = 0
        queue = deque()
        for i in range(len(deck)):
            queue.append(i)

        for i in range(len(deck)):
            result[queue.popleft()] = deck[ind]
            ind += 1
            if queue:
                queue.append(queue.popleft())
        
        return result
            

            