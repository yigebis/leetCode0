class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map or self.map[key][0][0] > timestamp:
            return ""
        nearest = ""
        for i in range(len(self.map[key]) - 1, -1, -1):
            if self.map[key][i][0] <= timestamp:
                nearest = self.map[key][i][1]
                break

        return nearest 
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)