def foo(x):
    print("executing foo(%s)"%(x))

class A(object):
    def foo(self,x):
        print("executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print("executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)"%x)

a=A()
a.foo('hello')

a.class_foo('hello')

a.static_foo('hello')