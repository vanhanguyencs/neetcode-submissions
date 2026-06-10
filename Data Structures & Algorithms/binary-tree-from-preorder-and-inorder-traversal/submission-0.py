# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def build(i, j, x, y):
            print(f'i: {i}, j: {j}, x: {x}, y: {y}')
            if i > j:
                return None
            if i == j:
                return TreeNode(preorder[i])
            
            root = TreeNode(preorder[i])
            idx = x
            while idx <= y:
                if inorder[idx] == preorder[i]:
                    break
                idx += 1
            """
            len of left: idx - x
            len of right: y - idx
            preorder
            left: [i + 1, i + idx - 1]
            right: [i + idx, y]
            inorder
            left: [x, idx - 1]
            right: [idx + 1, y]

            """
            len = idx - x
            root.left = build(i + 1, i + len, x, idx - 1)
            root.right = build(i + len + 1, j, idx + 1, y)
            return root
        
        n = len(preorder)
        return build(0, n - 1, 0, n - 1)
            
            
