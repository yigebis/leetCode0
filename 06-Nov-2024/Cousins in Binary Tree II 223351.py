# Problem: Cousins in Binary Tree II - https://leetcode.com/problems/cousins-in-binary-tree-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        queue.append(root)
        root.val = 0

        while queue:
            tot = 0
            for i in range(len(queue)):
                node = queue[i]
                queue[i] = [queue[i], 0]
                if node.left:
                    queue[i][1] -= node.left.val
                    tot += node.left.val
                if node.right:
                    queue[i][1] -= node.right.val
                    tot += node.right.val
            
            for i in range(len(queue)):
                node, val = queue.popleft()
                val += tot

                if node.left:
                    node.left.val = val
                    queue.append(node.left)
                if node.right:
                    node.right.val = val
                    queue.append(node.right)
        
        return root
                