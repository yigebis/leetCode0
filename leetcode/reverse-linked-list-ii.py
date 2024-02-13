# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverser(self, first):
        if not first or not first.next:
            return first
        prev, curr, next = None, first, first.next
        while next:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        curr.next = prev
        return curr
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        break1 = dummy
        count = 1
        while count < left:
            break1 = break1.next
            count += 1
        last = break1
        while count < right:
            last = last.next
            count += 1
        last = last.next
        break2 = last.next

        last.next = None 

        break1.next = self.reverser(break1.next)
        curr = break1
        while curr.next:
            curr = curr.next
        curr.next = break2
        # print(break1.val, break1.next.val, break2)
        return dummy.next

