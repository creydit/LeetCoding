# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = []
        def dfs(col,row,node):
            nodes.append((col,row,node.val))
            if node.left:
                dfs(col-1,row+1,node.left)
            if node.right:
                dfs(col+1,row+1,node.right)
        dfs(0,0,root)
        nodes.sort()
        ans = []
        temp = [nodes[0][2]]
        for i in range(1,len(nodes)):
            if nodes[i][0]==nodes[i-1][0]:
                temp.append(nodes[i][2])
            else:
                ans.append(temp)
                temp = [nodes[i][2]]
        ans.append(temp)
        return ans

