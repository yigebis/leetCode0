# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        while currA.next:
            currA = currA.next
        currA.next = headA
        slow, fast = headB, headB
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if not fast or not fast.next:
            currA.next = None
            return None
        
        first, second = headB, fast
        while True:
            if first == second:
                currA.next = None
                return first
            first = first.next
            second = second.next

        