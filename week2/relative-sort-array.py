class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # freq = defaultdict(int)
        # for i in arr1:
        #     freq[i] += 1
        # index = 0
        # arr1.sort()
        # for i in arr2:
        #     for j in range(freq[i]):
        #         arr1[index] = i
        #         index += 1
        precedence = {}
        for i in range(len(arr2)):
            precedence[arr2[i]] = i
        for num in arr1:
            if num not in precedence:
                precedence[num] = num + len(arr2)

        arr1.sort(key = lambda x : precedence[x])
        return arr1
