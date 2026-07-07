# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #Using Recursion and no extra space
        #TC - O(N) and SC - O(N) auxillary 
        if root is None or p==root or q==root:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l==None:
            return r
        elif r==None:
            return l
        return root 


        #DFS storing paths
        #TC - O(N+N) and SC - O(N+N)
        '''
        def dfs(node, x, path):
            if node is None:
                return False

            path.append(node)

            if node == x:
                return True

            if dfs(node.left,x,path):
                return True

            if dfs(node.right,x,path):
                return True
            path.pop()
            return False

        path1 = []
        path2 = []
        dfs(root, p, path1)
        dfs(root, q, path2)
        ans = None
        for i in range(min(len(path1), len(path2))):
            if path1[i] == path2[i]:
                ans = path1[i]
            else:
                break
        return ans
        '''