class Single:
    _instance = None
    def __new__(cls):
        if not cls._instance:
            cls._instance = super()
        return cls._instance


a = Single()
print(id(a))
b = Single()
print(id(b))