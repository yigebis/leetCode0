class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = 1000000.0
        maximum = 1000.0
        avg = 0
        count = 0
        for i in salary:
            minimum = min(minimum, i)
            maximum = max(maximum, i)
        for i in salary:
            if i != minimum  and i != maximum:
                avg += i
                count += 1
        avg /= count
        return avg