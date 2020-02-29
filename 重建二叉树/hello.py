# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        
        def build(preorder,inorder):
            if len(preorder)>0:
                root = TreeNode(preorder[0])
                ind = inorder.index(preorder[0])
                root.left = build(preorder[1:1+ind],inorder[:ind])
                root.right = build(preorder[1+ind:],inorder[ind+1:])
                return root
        return build(preorder,inorder)
s = Solution()
a = s.buildTree([3,9,20,15,7],[9,3,15,20,7])

def pri(a):
    if a == None:
        return
    if a != None:
        print(a.val)
    pri(a.left)
    pri(a.right)
    
    
pri(a)