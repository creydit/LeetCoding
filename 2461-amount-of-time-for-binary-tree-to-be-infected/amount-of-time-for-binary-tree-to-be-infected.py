# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        par = {root: None}
        q = deque()
        q.append(root)
        Rstart = -1
        while q:
            node = q.popleft()
            
            if node.val == start:
                Rstart = node
                
            if node.left:
                par[node.left] = node
                q.append(node.left)
                
            if node.right:
                par[node.right] = node
                q.append(node.right)
        
        vis = set()
        ans = 0
        q.append((Rstart,0))
        vis.add(Rstart)
        while q:
            node, lvl = q.popleft()
            ans = lvl
            for neigh in (node.left, node.right, par[node]):
                if neigh and neigh not in vis:
                    vis.add(neigh)
                    q.append((neigh, lvl+1))
        return ans