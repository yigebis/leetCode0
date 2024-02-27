"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        to_new = {}

        def next_generator(head):
            new_node = Node(0)
            if not head:
                new_node = None
                return new_node
            new_node.val = head.val
            new_node.next = next_generator(head.next)
            to_new[head] = new_node
            return new_node
        new_node = next_generator(head)
        curr = head
        while curr:
            print(curr.val)
            print(to_new[curr].val)
            if curr.random == None:
                to_new[curr].random = None
            else:
                to_new[curr].random = to_new[curr.random]
            curr = curr.next
        # print(new_node)  
        return new_node