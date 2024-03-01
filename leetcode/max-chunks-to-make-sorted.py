class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_chunks = 0

        # max_num = [arr[0]]
        # for i in range(1, len(arr)):
        #     max_num.append(max(arr[i], max_num[-1]))
        min_num = 0
        max_el = 0
        prev_chunk = -1
        covered = set()

        for r in range(len(arr)):
            covered.add(arr[r])
            max_el = max(max_el, arr[r])
            if min_num in covered and max_el - min_num + 1 == r - prev_chunk:
                max_chunks += 1
                while min_num in covered:
                    min_num += 1
                prev_chunk = r
        return max_chunks