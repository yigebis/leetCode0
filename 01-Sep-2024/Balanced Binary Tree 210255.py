# Problem: Balanced Binary Tree - https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def find_max_height(node):
            if not node:
                return (True, 0)
            
            max_left, max_right = find_max_height(node.left), find_max_height(node.right)
            if not max_left[0] or not max_right[0]:
                return (False, 0)

            if abs(max_left[1] - max_right[1]) > 1:
                return (False, 0)
            
            return (True, max(max_left[1], max_right[1]) + 1)
        
        return find_max_height(root)[0]
