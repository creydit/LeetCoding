# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def height(node):
            nonlocal ans
            if node==None:
                return 0
            lh = height(node.left)
            rh = height(node.right)
            ans = max(ans, lh+rh)
            return 1+max(lh,rh)
        hh = height(root)
        return ans