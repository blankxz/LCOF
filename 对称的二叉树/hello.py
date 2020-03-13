# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root.left,root.right)
        
    
    def dfs(self,l,r):
        if not l and not r:
            return True
        else:
            if l and r:
                if l.val!=r.val:
                    return False
                return self.dfs(l.left,r.right) and self.dfs(l.right,r.left)
            else:
                return False