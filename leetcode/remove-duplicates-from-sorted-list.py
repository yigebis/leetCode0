# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        left, right = head, head.next
        while right:
            while right and left.val == right.val:
                left.next = right.next
                right = left.next
            left = left.next
            if right:
                right = right.next
        return head
        