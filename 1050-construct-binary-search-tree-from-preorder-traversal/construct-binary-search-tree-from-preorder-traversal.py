# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #better finding inorder as it just sorted then constructing a with both of pre and in order
        #TC - O(nlogn) and SC - O(n)
        inorder = sorted(preorder)
        mp = {}
        for i, v in enumerate(inorder):
            mp[v] = i

        idx = 0
        
        def build(l,r):
            nonlocal idx
            if l>r:
                return None

            root = TreeNode(preorder[idx])
            idx += 1
            m = mp[root.val]
            root.left = build(l,m-1)
            root.right = build(m+1,r)
            return root

        return build(0,len(preorder)-1)

        #Brute force 
        #TC - O(N*N - N^2)
        '''
        def insert(v, root):
            node = TreeNode(v)
            if node.val < root.val:
                if root.left:
                    insert(v,root.left)
                else:
                    root.left = node
            else:
                if root.right:
                    insert(v, root.right)
                else:
                    root.right = node

        root = TreeNode(preorder[0])
        for i in range(1,len(preorder)):
            insert(preorder[i],root)
        return root
        '''
