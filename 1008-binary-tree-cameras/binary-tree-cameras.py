# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        inCams = set()
        ans = 0
        inCams.add(None)
        def dfs(node, par = None):
            nonlocal ans
            if node is None:
                return
            dfs(node.left, node)
            dfs(node.right,node)
            if (par is None and node not in inCams)  or (node.left not in inCams) or (node.right not in inCams):
                inCams.add(node)
                inCams.add(par)
                inCams.add(node.left)
                inCams.add(node.right)
                ans += 1
        dfs(root)
        return ans

        '''
        cams = 0
        def dfs(node):
            nonlocal cams
            if node is None:
                return 2
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0:
                cams += 1
                return 1
            if left == 1 or right == 1:
                return 2
            return 0
        if dfs(root) == 0:
            cams += 1
        return cams
        '''
            

            