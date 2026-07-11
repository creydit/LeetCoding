# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mp = {}
        for i, v in enumerate(inorder):
            mp[v] = i

        def build(ps, pe, ins, ine):
            if ps > pe:
                return None
            root = TreeNode(preorder[ps])
            k = mp[root.val]
            l = k - ins
            root.left = build(ps+1,ps+l,ins,k-1)
            root.right = build(ps+l+1,pe,k+1,ine)
            return root

        return build(0,len(preorder)-1,0,len(inorder)-1)