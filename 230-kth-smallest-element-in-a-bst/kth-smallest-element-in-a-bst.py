# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #Optimal using property of BST thatr inorder of BST is always sorted
        cnt = 0
        ans = None
        def dfs(node):
            nonlocal cnt
            nonlocal ans
            if node is None or ans is not None:
                return 
            dfs(node.left)
            cnt += 1
            if cnt == k:
                ans = node.val
                return
            dfs(node.right)
        dfs(root)
        return ans

        #Brute - sorting value in arr and finding
        #TC - O(NlogN) and SC - O(1)
        '''
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
        '''