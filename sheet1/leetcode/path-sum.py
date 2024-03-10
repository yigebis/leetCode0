# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        found = False
        def dfs(root, total):
            nonlocal found

            if not root:
                return
            if found:
                return
            total += root.val
            if not root.left and not root.right and total == targetSum:
                found = True
                return
            dfs(root.left, total)
            dfs(root.right, total)

        dfs(root, 0)
        if found:
            return True
        return False