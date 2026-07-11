# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        #TC - O(log^2N) and SC - O(H)
        if root is None:
            return 0
        def leftH(node):
            hh = 0
            while node:
                hh+=1
                node = node.left
            return hh
        
        def rightH(node):
            hh = 0
            while node:
                hh += 1
                node = node.right
            return hh
        
        lh = leftH(root)
        rh = rightH(root)

        if lh == rh: return 2**lh - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


        #TC -O(N) and SC - O(height of tree, auxillary)
        '''
        ans = 0
        def dfs(node):
            nonlocal ans
            if node is None:
                return 
            ans += 1
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ans 
        '''