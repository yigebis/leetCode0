# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root):
            if not root:
                return (None, False)
            if root.val == p.val or root.val == q.val:
                return (root, True)
            left = dfs(root.left)
            right = dfs(root.right)
            if left[1] and right[1]:
                # print(root.val)
                return (root, True)
            if left[1]:
                return (left[0], True)
            if right[1]:
                return (right[0], True)
            return (None, False)
        val = dfs(root)
        return val[0]