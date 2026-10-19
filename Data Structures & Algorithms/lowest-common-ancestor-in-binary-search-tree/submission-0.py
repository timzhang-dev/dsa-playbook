# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        current = root
        while True:
            if current.val == p.val:
                return current
            if current.val == q.val:
                return current
            if current.val > p.val and current.val < q.val:
                return current
            if current.val < p.val and current.val > q.val:
                return current
            if current.val < p.val and current.val < q.val:
                current = current.right
            if current.val > p.val and current.val > q.val:
                current = current.left
