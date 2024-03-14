class Solution:
    def possible(self, capacity, days):
        unit = 0
        curr_days = 1
        for weight in self.weights:
            unit += weight
            if unit > capacity:
                curr_days += 1
                unit = weight
        if curr_days > days:
            return False
        return True

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        self.weights = weights
        left, right = max(weights), sum(weights)
        least_capacity = right

        while left <= right:
            mid = left + (right - left) // 2
            if self.possible(mid, days):
                right = mid - 1
                least_capacity = mid
            else:
                left = mid + 1

        return  least_capacity