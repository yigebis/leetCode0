class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        total = 0

        total += min(k, numOnes)
        k -= min(k, numOnes)

        # total += min(k, numZeros)
        k -= min(k, numZeros)

        total -= min(k, numNegOnes)
        k -= min(k, numNegOnes)

        return total
        