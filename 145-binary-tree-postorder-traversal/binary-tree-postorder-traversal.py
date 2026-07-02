# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative
        if root==None:
            return []
        s1 = []
        s2 = []
        s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        ans =[]
        while s2:
            ans.append(s2.pop().val)
        return ans
        #Recrusive
        '''
        ans = []

        def postorder(node):
            if not node:
                return 
            
            postorder(node.left)
            postorder(node.right)
            ans.append(node.val)

        postorder(root)
        return ans 
        '''