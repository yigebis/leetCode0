# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0
        def dfs(root):
            nonlocal total

            if not root:
                return
            if root.val <= high and root.val >= low:
                total += root.val
                dfs(root.left)
                dfs(root.right)
                # print(root.val)
               
            if root.val < low:
                dfs(root.right)
            if root.val > high:
                dfs(root.left)
        
        dfs(root)

        return total