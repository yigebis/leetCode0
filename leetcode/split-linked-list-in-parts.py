# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        partitions = []
        node = head
        size = 0
        while node:
            node = node.next
            size += 1


        parts = k
        units = ceil(size/k)
        first_round = size % k
        second_round = parts - first_round
        new_head = head
        while first_round > 0:
            curr = new_head
            u = units
            while u > 1:
                curr = curr.next
                u -= 1
            partitions.append(new_head)
            new_head = curr.next
            curr.next = None

            first_round -= 1
        units = size // k
        while second_round:
            curr = new_head
            u = units
            while u > 1:
                curr = curr.next
                u -= 1
            partitions.append(new_head)
            if curr:
                new_head = curr.next
                curr.next = None

            second_round -= 1

        return partitions

