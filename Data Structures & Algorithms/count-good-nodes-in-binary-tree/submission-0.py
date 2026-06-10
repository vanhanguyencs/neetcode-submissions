# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        preorder: root, left, right
        carry: max_so_far
        """
        ans = []
        def preorder(node: TreeNode, max_so_far: int):
            nonlocal ans
            if not node:
                return
            print(max_so_far)
            if node.val >= max_so_far:
                ans.append(node.val)
            new_max = max(max_so_far, node.val)
            print(f'node: {node.val}. new_max: {new_max}')
            print(ans)
            preorder(node.left, new_max)
            preorder(node.right, new_max)

        preorder(root, float('-inf'))
        return len(ans)