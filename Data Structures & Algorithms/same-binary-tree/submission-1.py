# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.flag = True
        def dfs(current1, current2):
            if not current1 and not current2:
                return None
            if not current1 or not current2:
                self.flag = False
                return None


            dfs(current1.left, current2.left)
            dfs(current1.right, current2.right)

            if current1.val != current2.val:
                self.flag = False
            
            return current1, current2
        dfs(p, q)
        return self.flag
        