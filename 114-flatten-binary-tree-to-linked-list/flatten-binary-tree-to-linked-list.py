# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #Brute force using arr to store nodes and then creating nodes
        if root:
            arr = []
            def dfs(node):
                if node is None:
                    return
                arr.append(node)
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            curr = root
            for i in range(1,len(arr)):
                node = arr[i]
                curr.right = node
                curr.left = None
                curr = curr.right