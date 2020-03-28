class A:
    a = 1
    _b = 2
    def __init__(self):
        self._a = 'hello'

    def _aa(self):
        print('hhh')

a = A()
print(a._a)
a._aa()

print(A.a)
print(A._b)

__c = 1