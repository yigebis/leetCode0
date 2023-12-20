class OrderedStream:

    def __init__(self, n: int):
        self.stream = ["" for i in range(n)]
        self.ptr = 0
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey - 1] = value
        if self.stream[self.ptr] == "":
            return
        start = self.ptr
        while self.ptr < len(self.stream) and self.stream[self.ptr] != "":
            self.ptr += 1
        return self.stream[start:self.ptr]

        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)