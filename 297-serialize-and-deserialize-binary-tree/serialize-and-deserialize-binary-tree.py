# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return ''
        s = ""
        def dfs(node):
            nonlocal s
            s += str(node.val)+','
            if node.left:
                dfs(node.left)
            else:
                s += '#,'

            if node.right:
                dfs(node.right)
            else:
                s += '#,'
        dfs(root)
        return s

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        if len(data)==0:
            return []

        arr = data.split(',')
        root = TreeNode(int(arr[0]))
        idx = 1
        def dfs(node):
            nonlocal idx
            if idx >= len(arr)-1:
                return 

            if arr[idx] == '#':
                idx += 1
                node.left = None
            else:
                node.left = TreeNode(int(arr[idx]))
                idx += 1
                dfs(node.left)

            if arr[idx] == '#':
                idx += 1
                node.right = None
            else:
                node.right = TreeNode(int(arr[idx]))
                idx += 1
                dfs(node.right)
        dfs(root)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root)) 