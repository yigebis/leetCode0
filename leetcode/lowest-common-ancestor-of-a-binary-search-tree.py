# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative
        curr = root
        mini = min(p.val, q.val)
        maxi = max(p.val, q.val)
        while curr:
            if curr.val == p.val or curr.val == q.val:
                return curr
            if mini > curr.val:
                curr = curr.right
            elif maxi < curr.val:
                curr = curr.left
            else:
                return curr
        return curr