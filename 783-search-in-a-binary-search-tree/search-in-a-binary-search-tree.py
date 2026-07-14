# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return root
        
        def dfs(node):
            if node is None:
                return
            if node.val < val:
                return dfs(node.right)
            elif node.val > val:
                return dfs(node.left)
            else:
                return node
        
        return dfs(root)