# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder_successor(self,node):
        parent = node
        curr = node.right
        while curr.left:
            parent = curr
            curr = curr.left
        if curr.right:
            if parent.val > curr.val:
                parent.left = curr.right
            else:
                parent.right = curr.right
        else:
            if parent.val > curr.val:
                parent.left = None
            else:
                parent.right = None
        return curr.val
    # def min_on_right(self,node):
        # min_val = 100001
        # curr = node.right

        # while curr:
        #     min_val = min(min_val, curr.val)
        #     curr = curr.left

        # return min_val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        dummy = TreeNode(100001)
        dummy.left = root
        parent = dummy
        curr = root

        while curr:
            if key > curr.val:
                parent = curr
                curr = curr.right
            elif key < curr.val:
                parent = curr
                curr = curr.left
            else:
                if not curr.left and not curr.right:
                    if curr.val > parent.val:
                        parent.right = None
                    else:
                        parent.left = None
                elif not curr.right:
                    if curr.val > parent.val:
                        parent.right = curr.left
                    else:
                        parent.left = curr.left
                elif not curr.left:
                    if curr.val > parent.val:
                        parent.right = curr.right
                    else:
                        parent.left = curr.right
                else:
                    inorder_succ = self.inorder_successor(curr)
                    curr.val = inorder_succ
                    # delete the node which contains the maximum value on the left
                    # sub_tree
                    # parent = curr
                    # curr = curr.right
                    # while curr.left:
                    #     curr = curr.left
                    
                    # if not inorder_succ.right:
                        
                break
        return dummy.left
        # case 1 d