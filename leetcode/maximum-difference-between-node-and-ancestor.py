# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def __init__(self):
    #     self.min_val = 100001
    #     self.max_val = 0
    #     self.max_diff = 0 
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:


        def dfs(root, max_val, min_val):
            if not root:
                return max_val - min_val

            max_val = max(max_val, root.val)
            min_val = min(min_val, root.val)
            # print(max_val, min_val)

            left_diff = dfs(root.left, max_val, min_val)
            right_diff = dfs(root.right, max_val, min_val)

            return max(left_diff, right_diff) 
        return dfs(root, 0, 100000)