# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, biggest):
            nonlocal good
            if not node:
                return
            
            if node.val >= biggest:
                good += 1
                
            maxVal = max(node.val, biggest)
            dfs(node.left, maxVal)
            dfs(node.right, maxVal)
        good = 0
        dfs(root, root.val)
        return good

        

        
