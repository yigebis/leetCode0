class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        min_ops = 0
        while target > startValue:
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
            min_ops += 1
        if target < startValue:
            min_ops += startValue - target
        return min_ops