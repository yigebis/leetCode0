# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.arr = []
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.inorder(root)
        print(self.arr)
        for i in range(1, len(self.arr)):
            if self.arr[i] <= self.arr[i-1]:
                return False
        return True
            