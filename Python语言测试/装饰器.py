def a(f):
    
    print("print_a")
    def print_b():
        print("print_b")
    return print_b

@a
def f():
    print("print_f")
    
f()