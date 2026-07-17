# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        #Brute force 
        #TC - O(N*N - N^2)
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
