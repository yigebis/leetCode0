# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        curr = node
        prev = None
        while curr.next:
            prev = curr
            curr.val = curr.next.val
            curr = curr.next
        prev.next = None
        
        