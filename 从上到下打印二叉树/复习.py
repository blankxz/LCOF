# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root :
            return []
        res = []
        a = [root]
        while a:
            r = a.pop(0)    
            res.append(r.val)
            if r.left:
                a.append(r.left)
            if r.right:
                a.append(r.right)
        return res