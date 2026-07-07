# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        mp = defaultdict(int)
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