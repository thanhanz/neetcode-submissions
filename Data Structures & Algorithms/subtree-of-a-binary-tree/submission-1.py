# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        
        if root is None:
            return False

        main_stack = [root]

        '''
        - Edge cases (root before be sent are already equal - check left/right)
        '''

        def isSame(root, sub_root):
            stack = [(root, sub_root)]
            
            while stack:
                root, sub = stack.pop()

                if root is None and sub is None:
                    continue
                
                # Not equal
                if root is None or sub is None:
                    return False
                
                # Not equal
                if root.val != sub.val:
                    return False

                stack.append((root.left, sub.left))
                stack.append((root.right, sub.right))

            return True



        while main_stack:        
            current = main_stack.pop()

            if current.val == subRoot.val:
                # Compare that root (first lookup)
                if isSame(current, subRoot):
                    return True

            if current.left is not None:
                main_stack.append(current.left)

            if current.right is not None:
                main_stack.append(current.right)
            
        return False