class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plant_grow = []
        for i in range(len(plantTime)):
            plant_grow.append((plantTime[i], growTime[i]))
        
        plant_grow.sort(key = lambda x : -x[1])

        total_seed = 0
        max_days = 0
        for time in plant_grow:
            total_seed += time[0]
            max_days = max(max_days, total_seed + time[1])
        
        return max_days

