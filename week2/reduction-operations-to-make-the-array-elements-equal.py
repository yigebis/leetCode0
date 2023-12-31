class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        # 11223344
        # 44332211
        # 4 : 2, 3 : 2, 2: 2, 1 : 2
        # len = 4, so start from 3
        # 3 * freq (4) + 2 * freq(3) + 1 * freq(2) + 0 * freq(1)
        # 11223, 32211
        # len = 3
        # 2 * 1 + 1 * 2 + 0 * 2
        count = 0
        nums.sort(reverse=True)
        freq = {}
        seen = set()
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        downgrade = len(freq) - 1
        for i in nums:
            if i not in seen:
                count += downgrade * freq[i]
                downgrade -= 1
                seen.add(i)
        return count
