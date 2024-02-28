# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        index = 0
        val = root.val
        found = False

        def dfs(root):
            nonlocal index
            nonlocal val, found

            if not root:
                return
            if found:
                return
            dfs(root.left)
            index += 1
            if index == k:
                val = root.val
                found = True
            
            dfs(root.right)
        dfs(root)
        return val
            
            
            