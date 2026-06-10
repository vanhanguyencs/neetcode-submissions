# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        preorder: root, left, right
        carry: min_val, max_val
        condition: root.val > min_val or root.val < max_val: return False
        else return isValid(root.left, min_val, max(max_val, root.val))
        and isValid(root.right, min(min_val, root.val), max_val)
        """

        def isValid(node: TreeNode, min_val=float('-inf'), max_val=float('inf')) -> bool:
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (isValid(node.left, min_val, node.val)
                    and isValid(node.right, node.val, max_val)
                    )
        return isValid(root, float('-inf'), float('inf'))

        