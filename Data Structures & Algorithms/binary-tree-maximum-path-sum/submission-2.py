# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def max_path_down(node):
            nonlocal ans
            if not node:
                return 0
            l = max(max_path_down(node.left), 0)
            r = max(max_path_down(node.right), 0)
            ans = max(ans, node.val + l + r)
            return node.val + max(l, r)
        max_path_down(root)
        return ans