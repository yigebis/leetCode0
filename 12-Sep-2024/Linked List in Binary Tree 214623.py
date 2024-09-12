# Problem: Linked List in Binary Tree - https://leetcode.com/problems/linked-list-in-binary-tree/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def dfs(tree_node : Optional[TreeNode], list_node : Optional[ListNode]):
            if not list_node:
                return True
            if not tree_node:
                return False

            if tree_node.val == list_node.val:
                left_res = dfs(tree_node.left, list_node.next)
                if left_res:
                    return True
                right_res = dfs(tree_node.right, list_node.next)
                return right_res
            
            return False

        queue = deque([root])

        while queue:
            curr = queue.popleft()
            if dfs(curr, head):
                return True
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        
        return False
