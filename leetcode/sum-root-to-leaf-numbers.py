# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        def dfs(root, string):
            if not root:
                return
            nonlocal total_sum

            if not root.left and not root.right:
                string += str(root.val)
                total_sum += int(string)
                return
            string += str(root.val)
            dfs(root.left, string)
            dfs(root.right, string)
        dfs(root, "")
        return total_sum