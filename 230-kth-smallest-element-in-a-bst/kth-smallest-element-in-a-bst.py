# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Brute - sorting value in arr and finding
        #TC - O(NlogN) and SC - O(1)
        arr = []
        def dfs(node):
            if node is None:
                return 
            arr.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        arr.sort()
        return arr[k-1]