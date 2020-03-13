class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = []
        while popped:
            if pushed!=[]:
                a = pushed.pop(0)
                res.append(a)
            while res and popped:
                if res[-1] == popped[0]:
                    res.pop()
                    popped.pop(0)
                elif pushed == []:
                    return False
                else:
                    break
        if res:
            return False
        else:
            return True