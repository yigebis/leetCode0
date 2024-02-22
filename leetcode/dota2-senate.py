class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q = deque()
        d_wait = 0
        r_wait = 0
        dires = 0
        radiants = 0
        for s in senate:
            if s == 'D':
                dires += 1
            else:
                radiants += 1
            q.append(s)
        
        while dires > 0 and radiants > 0:
            if q[0] == 'D':
                if d_wait == 0:
                    q.append(q.popleft())
                    r_wait += 1
                else:
                    q.popleft()
                    dires -= 1
                    d_wait -= 1
            else:
                if r_wait == 0:
                    q.append(q.popleft())
                    d_wait += 1
                else:
                    q.popleft()
                    radiants -= 1
                    r_wait -= 1
        if radiants > 0:
            return "Radiant"
        return "Dire"   


        
            
