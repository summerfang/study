class Singleton:
    _instance = None

    def __new__(cls1, *args, **kwargs):
        if not cls1._instance:
            cls1._instance = super(Singleton, cls1).__new__(cls1, *args, **kwargs)
        return cls1._instance
    
    def __init__(self1):
        self1.value = 42

singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True
print(singleton1.value)  # 42