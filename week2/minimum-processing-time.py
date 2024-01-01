class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        minTime = 0

        for i in range(len(processorTime)):
            minTime = max(minTime, processorTime[i] + tasks[i + 3*(i+1)])
        return minTime

