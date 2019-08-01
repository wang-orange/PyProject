import time

# 装饰器用来为一个函数实现新的功能，但不改变原函数的代码和调用方式

def decorator(fun):
    def wrapper():
        print(time.time())
        fun()
    return wrapper

@decorator
def f1():
    print('This is function')

# f = decorator(f1)
# f()

# 装饰器的作用：保持原函数的调用方式
f1()