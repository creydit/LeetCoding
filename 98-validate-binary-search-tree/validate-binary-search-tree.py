# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,lr,rr):
            if node is None:
                return True
            if node.val >= rr or node.val <= lr:
                return False
            l = dfs(node.left,lr,node.val)
            r = dfs(node.right,node.val,rr)
            return l and r

        return dfs(root,-10**18,10**18)
