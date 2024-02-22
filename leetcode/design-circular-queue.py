class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [0 for i in range(k)]
        self.size = 0
        self.f = -1
        self.r = -1

    def enQueue(self, value: int) -> bool:
        if self.size == len(self.q):
            return False
        self.r = (1 + self.r) % len(self.q)
        self.q[self.r] = value
        if self.f == -1:
            self.f += 1
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.q[self.f] = 0
        self.f = (1 + self.f) % len(self.q)
        self.size -= 1
        if self.size == 0:
            self.r, self.f = -1, -1
        
        return True

        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.f]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.r]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == len(self.q)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()