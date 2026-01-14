# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -10**18
        def solve(node):
            nonlocal ans
            if node is None:
                return 0
            
            l = solve(node.left)
            r = solve(node.right)

            ans1 = l + r + node.val
            ans2 = max(l,r) + node.val
            ans3 = node.val

            ans = max([ans,ans1,ans2,ans3])
            return max(ans2,ans3)
        
        solve(root)
        return ans 
        
