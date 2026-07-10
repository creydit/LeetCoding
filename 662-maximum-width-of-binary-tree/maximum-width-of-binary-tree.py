# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque()
        q.append((root,0))
        ans = 0
        while q:
            f = q[0][1]
            l = q[-1][1]
            ans = max(ans, l-f+1)
            for _ in range(len(q)):
                node,idx = q.popleft()
                idx = idx-f 
                if node.left:
                    q.append((node.left,2*idx))
                if node.right:
                    q.append((node.right, 2*idx + 1))
        return ans
