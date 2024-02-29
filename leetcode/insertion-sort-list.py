# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removed(self, parent, curr):
        parent.next = curr.next
        curr.next = None
        return curr
    def insert(self, back, curr):
        curr.next = back.next
        back.next = curr
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        dummy = ListNode(-5000)
        dummy.next = head
        curr = head.next
        parent = head

        while curr:
            # find the node upto curr where the value is greater
            added = False
            back, trav = dummy, dummy.next
            while trav and trav != curr:
                if trav.val > curr.val:
                    curr = self.removed(parent, curr)
                    self.insert(back, curr)
                    added = True
                    curr = parent.next
                    break
                back = trav
                trav = trav.next
            if not added:
                parent = curr
                curr = curr.next
            
        return dummy.next