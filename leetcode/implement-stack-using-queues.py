class MyStack:

    def __init__(self):
        self.queue = deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        for i in range(1, len(q)):
            q.append(q.popleft())
            
    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

'''
[1,2,3]
[1,2,3,4]
[1,2,3,4,1] -> [2,3,4,1]
[2,3,4,1,2] -> [3,4,1,2]
'''