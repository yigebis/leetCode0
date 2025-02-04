# Problem: Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = -inf

        def maxSumWithConnector(node):
            nonlocal max_path_sum

            if not node:
                return 0

            curr_sum = node.val
            left_max = maxSumWithConnector(node.left)
            right_max = maxSumWithConnector(node.right)

            if left_max > 0:
                curr_sum += left_max

            if right_max > 0:
                curr_sum += right_max
            
            max_path_sum = max(max_path_sum, curr_sum)

            if curr_sum == node.val:
                return curr_sum
            
            return node.val + max(left_max, right_max)
        
        maxSumWithConnector(root)

        return max_path_sum
            
