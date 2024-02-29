# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        def builder(nums):
            if not nums:
                return
            max_idx = 0
            for i in range(len(nums)):
                if nums[i] > nums[max_idx]:
                    max_idx = i
            root = TreeNode(nums[max_idx])
            root.left = builder(nums[0 : max_idx])
            root.right = builder(nums[max_idx + 1 : ])

            return root
        return builder(nums)