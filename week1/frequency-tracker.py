class FrequencyTracker:
    # 2 3
    # 2 : 0 3 : 1
    
    def __init__(self):
        # self.index = {}
        self.count = defaultdict(int)
        self.frequency = defaultdict(int)

    def add(self, number: int) -> None:
        self.frequency[number] += 1
        self.count[self.frequency[number]] += 1
        self.count[self.frequency[number] - 1] -= 1

    def deleteOne(self, number: int) -> None:
        if self.frequency[number] == 0:
            return
        self.count[self.frequency[number]] -= 1
        self.count[self.frequency[number] - 1] += 1
        self.frequency[number] -= 1

    def hasFrequency(self, freq: int) -> bool:
        if self.count[freq] > 0:
            return True
        return False

    # 1 2 3 4 4 4

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)