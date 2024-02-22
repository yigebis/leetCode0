# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # recursion    
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iterative - stack
        max_depth = 0
        stack = [(root, 1)]
        while stack:
            node_depth = stack.pop()
            node, depth = node_depth[0], node_depth[1]
            max_depth = max(max_depth, depth)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        
        return max_depth
