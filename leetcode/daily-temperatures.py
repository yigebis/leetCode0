class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # warmer = {}
        days_to_wait = [0 for i in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                days_to_wait[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)

        return days_to_wait

