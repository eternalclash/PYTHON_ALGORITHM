class Solution(object):
    def inorderTraversal(self, root):
        arr=[]
        def dfs(root):
            if root:
                dfs(root.left)
                arr.append(root.val)
                dfs(root.right)
        dfs(root)
        return arr