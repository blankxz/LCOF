# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        a = []
        a.append(root)
        res = []
        while a:
            tem = []
            b = []
            for i in a:
                tem.append(i.val)
                if i.left:
                    b.append(i.left)
                if i.right:
                    b.append(i.right)
            res.append(tem)
            a = b
        return res