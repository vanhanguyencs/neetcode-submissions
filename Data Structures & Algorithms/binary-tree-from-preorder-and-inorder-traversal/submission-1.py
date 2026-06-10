# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        def build(i, j, x, y):
            if i > j:
                return None
            if i == j:
                return TreeNode(preorder[i])
            
            root = TreeNode(preorder[i])
            idx = inorder_index[preorder[i]]
            left_size = idx - x
            root.left = build(i + 1, i + left_size, x, idx - 1)
            root.right = build(i + left_size + 1, j, idx + 1, y)
            return root
        
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
            
            
