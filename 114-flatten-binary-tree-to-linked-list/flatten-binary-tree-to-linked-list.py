# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        #using stack same TC - O(N) and SC - O(N)
        #can be done by recursion too
        if root is None:
            return
        st = []
        st.append(root)
        while st:
            curr = st.pop()
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
            if st:
                curr.right = st[-1]
            curr.left = None

        #Brute force using arr to store nodes and then creating nodes
        #TC - O(N) and SC - O(N)
        '''
        if root:
            arr = []
            def dfs(node):
                if node is None:
                    return
                arr.append(node)
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            curr = root
            for i in range(1,len(arr)):
                node = arr[i]
                curr.right = node
                curr.left = None
                curr = curr.right
        '''