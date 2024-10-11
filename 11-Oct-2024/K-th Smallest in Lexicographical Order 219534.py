# Problem: K-th Smallest in Lexicographical Order - https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/

class Solution:
    # 1 - 111
    # 45
    def findKthNumber(self, n: int, k: int) -> int:
        ans = -1

        def count_tots_with_prefix(node):
            count = 0
            nxt = node + 1

            while node <= n:
                count += min(nxt, n+1) - node
                node *= 10
                nxt *= 10
            
            return count


        def dfs(node, start, tot):
            # print(node, start, tot)
            nonlocal ans
            if start == k:
                ans = node
                return
            if k > tot:
                return
            if node > n:
                return

            nxt_start = start + 1
            nxt_tot = start

            for i in range(10):
                nxt_node = node * 10 + i
                nxt_tot += count_tots_with_prefix(nxt_node)
                dfs(nxt_node, nxt_start, nxt_tot)
                if ans != -1:
                    return
                nxt_start = nxt_tot + 1
        
        start = 1
        tot = 0

        # print(count_tots_with_prefix(1))
        for i in range(1, 10):
            tot += count_tots_with_prefix(i)
            dfs(i, start, tot)
            if ans != -1:
                break
            start = tot + 1

        return ans

        