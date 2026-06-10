# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        inorder: left root right
        count from one until k
        """
        ans = -1
        count = 0
        def inorder(node):
            if not node:
                return
            nonlocal ans
            nonlocal count
            inorder(node.left)
            count += 1
            if count == k:
                ans = node.val
            inorder(node.right)
        
        inorder(root)
        return ans
