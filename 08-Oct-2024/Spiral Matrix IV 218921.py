# Problem: Spiral Matrix IV - https://leetcode.com/problems/spiral-matrix-iv/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        spiral = [[-1 for i in range(n)] for j in range(m)]

        def horiz_right(x, y, node):
            while y < n and node:
                if spiral[x][y] != -1:
                    break
                spiral[x][y] = node.val
                y += 1
                node = node.next
            
            return x + 1, y - 1, node
        
        def vert_down(x, y, node):
            while x < m and node:
                if spiral[x][y] != -1:
                    break
                spiral[x][y] = node.val
                x += 1
                node = node.next
            
            return x - 1, y - 1, node
        
        def horiz_left(x, y, node):
            while y > -1 and node:
                if spiral[x][y] != -1:
                    break
                spiral[x][y] = node.val
                y -= 1
                node = node.next
            
            return x - 1, y + 1, node
        
        def vert_up(x, y, node):
            while x > -1 and node:
                if spiral[x][y] != -1:
                    break
                spiral[x][y] = node.val
                x -= 1
                node = node.next
            
            return x + 1, y + 1, node
        
        x, y, node = 0, 0, head
        while node:
            if node:
                x, y, node = horiz_right(x, y, node)
            if node:
                x, y, node = vert_down(x, y, node)
            if node:
                x, y, node = horiz_left(x, y, node)
            if node:
                x, y, node = vert_up(x, y, node)
        
        return spiral
        