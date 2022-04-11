class Solution(object):
    def postorderTraversal(self, root):
        arr = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                arr.append(node.val)
        dfs(root)
        return arr
    