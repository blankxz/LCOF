class A:
    def fun1(self):
        print("fun1")

def fun2():
    print("fun2")

def fun3():
    print("fun3")

a = A()
a.fun1()
a.fun1 = fun2

a.fun1()

fun2 = fun3

fun2()