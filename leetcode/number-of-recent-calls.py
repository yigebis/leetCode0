class RecentCounter:

    def __init__(self):
        self.queue = []
        self.l = 0
        self.r = -1

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.r += 1
        while self.queue[self.l] < t - 3000:
            self.l += 1
        return self.r - self.l + 1
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)