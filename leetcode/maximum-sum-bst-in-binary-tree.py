# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        def dfs(root):
            nonlocal max_sum
            if not root:
                return 
            if not root.left and not root.right:
                max_val, min_val, sub_sum = root.val, root.val, root.val
                max_sum = max(max_sum, sub_sum)
                return (max_val, min_val, sub_sum, True)

            left = dfs(root.left)
            right = dfs(root.right)

            min_val = root.val
            max_val = root.val
            sub_sum = root.val
            if left and right:
                if left[3] == right[3] == True and root.val > left[0] and root.val < right[1]:
                    sub_sum = root.val + left[2] + right[2]
                    min_val, max_val = left[1], right[0]
                    max_sum = max(max_sum, sub_sum)
                    status = True
                else:
                    status = False
            elif left:
                if left[3] == True and root.val > left[0]:
                    sub_sum = root.val + left[2]
                    min_val = left[1]
                    max_sum = max(max_sum, sub_sum)
                    status = True
                else:
                    status = False
            elif right:
                if right[3] == True and root.val < right[1]:
                    sub_sum = root.val + right[2]
                    max_val = right[0]
                    max_sum = max(max_sum, sub_sum)
                    status = True
                else:
                    status = False
                
            
            return (max_val, min_val, sub_sum, status)
        
        dfs(root)
        return max_sum

                # max_val = root.val, min_val = root.val
                # update the global max_sum
                # return 
            # call dfs to the right and left
            # if status is true in both cases
            # check if the minimum on the right is > root.val 
            # and the maximum on the left is < root.val. 
            # If so, update the max_sum as the sum of root.val and max_sums on the two calls
            # min_val = min(first_min_val and second_min_val) and so for max_val
            # return (min_val, max_val, status, sum_so_far)
