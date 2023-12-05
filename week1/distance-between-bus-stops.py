class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:

        direct_path = 0
        total_sum = sum(distance)

        for i in range(min(start, destination), max(start, destination)):
            direct_path += distance[i]
        
        indirect_path = total_sum - direct_path

        return min(direct_path, indirect_path)