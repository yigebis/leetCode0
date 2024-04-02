# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.asc = []
        to_node = {}
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.asc.append(root.val)
            to_node[len(self.asc) - 1] = root
            inorder(root.right)
        inorder(root)
        for i in range(len(self.asc) - 2, -1, -1):
            self.asc[i] += self.asc[i+1]
            to_node[i].val = self.asc[i]
        
        return root
        