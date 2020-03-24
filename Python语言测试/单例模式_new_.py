class Singleton(object):
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)  
        return cls._instance 
    
a = Singleton()
print(id(a))
b = Singleton()
print(id(b))    



class hello(object):
    def __init__(self,a):
        pass
        
    def __new__(cls,*args,**kwargs):
        print(args)
        print(kwargs)
        return super().__new__(cls)
    
a = hello('a')