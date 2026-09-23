# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursion
        # ----------------------------------------------------------------------
        # if root is None:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # Level-order (BFS)
        # ----------------------------------------------------------------------    
        if not root:
            return 0

        queue = [root]
        depth = 0
        while queue:
            depth += 1
            next_level = []
            for node in queue:
                if node.left is not None:
                    next_level.append(node.left)
                if node.right is not None:
                    next_level.append(node.right)
            
            queue = next_level

        return depth