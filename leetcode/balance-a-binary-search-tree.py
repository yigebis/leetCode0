# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        to_list = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            to_list.append(root.val)
            inorder(root.right)
        def appender(nums):
            if not nums:
                return
            mid = (len(nums) - 1)//2
            root = TreeNode(nums[mid])
            root.left = appender(nums[0 : mid])
            root.right = appender(nums[mid + 1 : ])

            return root
        inorder(root)
        return appender(to_list)
