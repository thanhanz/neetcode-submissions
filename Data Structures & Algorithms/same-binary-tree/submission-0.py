# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True

        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False

        queue = [[p, q]]
        
        # queue pop(0) - append()
        while queue:
            current = queue.pop(0)

            if ((current[0].left is None and current[1].left is not None) 
                or 
                (current[0].left is not None and current[1].left is None)):
                return False
            
            if ((current[0].right is None and current[1].right is not None) 
                or 
                (current[0].right is not None and current[1].right is None)):
                return False
            
            if (current[0].left is not None and current[1].left is not None):
                queue.append((current[0].left, current[1].left))

            if (current[0].right is not None and current[1].right is not None):
                queue.append((current[0].right, current[1].right))

            if current[0].val != current[1].val:
                return False
        
        return True

