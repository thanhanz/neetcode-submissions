# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Recursion solution
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # if root is None:
        #     return None
        
        # left_node = self.invertTree(root.left)
        # right_node = self.invertTree(root.right)

        # root.left = right_node
        # root.right = left_node

        # return root
        if root is None:
            return None
        queue = [] #append() and pop()   <= [ 1 | 0 | 0 | 1 ] <=

        queue.append(root)

        while queue:
            top = queue.pop(0)
            
            #Swap
            temp = top.left
            top.left = top.right
            top.right = temp

            if top.left is not None:
                queue.append(top.left)
            if top.right is not None:
                queue.append(top.right)
        
        return root
            



