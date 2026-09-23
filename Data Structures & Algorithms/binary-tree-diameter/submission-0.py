# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Find max edges each nodes (left + right)
        stack = [root] # append() and pop() but queue is pop(0)
        mp = {} # map store [value : longest path of that node]
        longest_path = 0
        # DFS

        while stack:
            current_node = stack[-1]
            # Handle add child to stack till end
            if current_node.left is not None and current_node.left not in mp:
                stack.append(current_node.left)
            elif current_node.right is not None and current_node.right not in mp:
                stack.append(current_node.right)
            # No child
            else:
                # Handle max(left, right)
                top = stack.pop()
                longest_left = mp.get(top.left, 0)
                longest_right = mp.get(top.right, 0)
                
                mp[top] = 1 + max(longest_left, longest_right)
                longest_path = max(longest_path, longest_left + longest_right)
        
        return longest_path


        