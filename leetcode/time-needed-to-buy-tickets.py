class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # val = tickets[k]
        # time = 0
        # for i in range(len(tickets)):
        #     if i > k:
        #         tickets[i] -= (val - 1)
        #         if tickets[i] > 0:
        #             time += val - 1
        #         else:
        #             time += val - 1 - tickets[i]
        #     else:
        #         tickets[i] -= val
        #         if tickets[i] > 0:
        #             time += val
        #         else:
        #             time += val + tickets[i]
        # return time
        time = 0
        q = deque()
        for i in range(len(tickets)):
            q.append(i)
        while tickets[k] > 0:
            tickets[q[0]] -= 1
            if tickets[q[0]] == 0:
                q.popleft()
            else:
                q.append(q.popleft())
            time += 1
        
        return time