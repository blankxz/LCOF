class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder)<=2:
            return True
        n=len(postorder)
        root=postorder[-1]
        
        for i in range(n):
            if postorder[i]>root:
                break
        for j in range(i+1,n-1):
            if postorder[j]<root:
                return False

        return self.verifyPostorder(postorder[:i]) and self.verifyPostorder(postorder[i:n-1])###
