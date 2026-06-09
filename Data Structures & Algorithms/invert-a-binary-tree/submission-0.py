# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        left = right = None
        if root.left:
            right = self.invertTree(root.left)
        if root.right:
            left = self.invertTree(root.right)
        
        root.left = left
        root.right = right
        return root
