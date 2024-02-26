# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        column = defaultdict(list)
        self.min_col, self.max_col = 0, 0

        def dfs(root, col, row):
            if not root:
                return
            column[col].append((root.val, row))
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            dfs(root.right, col + 1, row + 1)
            dfs(root.left, col - 1, row + 1)
        dfs(root, 0, 0)
        for i in range(self.min_col, self.max_col + 1):
            column[i].sort(key=lambda x : (x[1], x[0]))
            for _ in range(len(column[i])):
                column[i][_] = column[i][_][0]
            output.append(column[i])
        
        return output