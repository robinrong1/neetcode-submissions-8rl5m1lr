# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def height(root):
            if root is None:
                return 0
            myHeight = max(height(root.left), height(root.right))
            return myHeight + 1

        if abs(height(root.left) - height(root.right)) > 1:
            return False
        else:
            return True