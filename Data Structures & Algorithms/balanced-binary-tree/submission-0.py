# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def max_height(root):

            if not root:
                return 0
            
            max_root_left = max_height(root.left)
            max_root_right = max_height(root.right)

            if not abs(max_root_left - max_root_right) <= 1:
                balanced[0] = False
                return 0

            return 1 + max(max_root_left, max_root_right)
        
        max_height(root)
        return balanced[0]

