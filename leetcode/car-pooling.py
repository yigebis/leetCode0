class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_destination = 0
        for trip in trips:
            max_destination = max(max_destination, trip[2])

        passengers = [0 for i in range(max_destination + 1)]
        for num_passengers, fro, to in trips:
            passengers[fro] += num_passengers
            passengers[to] -= num_passengers
        
        if passengers[0] > capacity:
            return False
        for i in range(1, len(passengers)):
            passengers[i] += passengers[i-1]
            if passengers[i] > capacity:
                return False
        return True