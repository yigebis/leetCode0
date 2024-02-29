# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        min_at_row, max_at_row = {}, {}

        def dfs(root, row, col):
            if not root:
                return
            max_at_row[row] = max(max_at_row.get(row, col), col)
            min_at_row[row] = min(min_at_row.get(row, col), col)
            dfs(root.left, row + 1, col * 2)
            dfs(root.right, row + 1, col * 2 + 1)
        dfs(root, 0, 0)
        max_width = 0

        for r in min_at_row:
            max_width = max(max_width, max_at_row[r] - min_at_row[r] + 1)
        
        return max_width
        