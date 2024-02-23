# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.merged = TreeNode()
        self.curr = self.merged
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        merged = TreeNode()
        # curr = merged
        def dfs(curr, root1, root2):
            if not root1:
                return root2
            if not root2:
                return root1
            curr.val = root1.val + root2.val
            print(curr.val)
            curr.left = TreeNode()
            curr.left = dfs(curr.left, root1.left, root2.left)
            curr.right = TreeNode()
            curr.right = dfs(curr.right, root1.right, root2.right)
            return curr
        merged = dfs(merged, root1, root2)
        return merged


