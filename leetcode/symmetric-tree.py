# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if not root.left and not root.right:
        #     return True
        # if (root.left and not root.right) or (root.right and not root.left):
        #     return False
        # node_left_right(root.left)
        # node_right_left(root.right)

        # if len(lr) != len(rl)
        # if root.right.val != root.left.val:
        #     return False
        # return self.isSymmetric(root.left) and self.isSymmetric(root.right)

        def dfs(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 and root2 or not root2 and root1:
                return False
            if root1.val != root2.val:
                return False
            return dfs(root1.right, root2.left) and dfs(root1.left, root2.right)
        return dfs(root, root)