# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # balanced = [True]

        # def max_height(root):

        #     if not root:
        #         return 0
            
        #     max_root_left = max_height(root.left)
        #     max_root_right = max_height(root.right)

        #     if not abs(max_root_left - max_root_right) <= 1:
        #         balanced[0] = False
        #         return 0

        #     return 1 + max(max_root_left, max_root_right)
        
        # max_height(root)
        # return balanced[0]
        
        # ================================================
        if not root:
            return True

        stack = [(root, False)]
        heights = {}

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                left_height = heights.get(node.left, 0)
                right_height = heights.get(node.right, 0)

                if abs(left_height - right_height) > 1:
                    return False

                heights[node] = 1 + max(left_height, right_height)

            else:
                # Process this node AFTER its children
                stack.append((node, True))

                stack.append((node.right, False))
                stack.append((node.left, False))

        return True
