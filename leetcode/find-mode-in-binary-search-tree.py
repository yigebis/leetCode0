# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        max_freq = 0

        def fillDict (root):
            nonlocal max_freq

            if not root:
                return 
            freq[root.val] += 1
            max_freq = max(max_freq, freq[root.val])
            fillDict(root.left)
            fillDict(root.right)
        
        fillDict(root)
        modes = []
        for val in freq:
            if freq[val] == max_freq:
                modes.append(val)
        return modes
