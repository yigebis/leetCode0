# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        zigzag = []
        at_row = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        curr = root
        max_row = 0

        while queue:
            curr = queue.popleft()
            node = curr[0]
            row = curr[1]

            if not node:
                continue
            max_row = max(max_row, row)
            at_row[row].append(node.val)
            queue.append((node.left, row + 1))
            queue.append((node.right, row + 1))
        for i in range(0, max_row + 1):
            arr = at_row[i][:]
            # print(arr)
            
            if i % 2:
                arr.reverse()
                zigzag.append(arr)
            else:
                zigzag.append(arr)
        return zigzag