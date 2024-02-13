# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy1, dummy2 = ListNode(), ListNode()
        less, greater = dummy1, dummy2
        pointer = head
        while pointer:
            if pointer.val < x:
                less.next = pointer
                less = less.next
            else:
                greater.next = pointer
                greater = greater.next
            pointer = pointer.next
        less.next = None
        greater.next = None
        less.next = dummy2.next
        head = dummy1.next
        return head
        
        