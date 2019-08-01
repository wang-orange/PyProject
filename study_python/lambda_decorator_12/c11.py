# 装饰器，原函数带参数，并且被装饰的函数的参数列表可变
import time

def decorator(fun):
    def wrapper(*args, **kw):
        print(time.time())
        fun(*args, **kw)
    return wrapper

@decorator
def f0():
    print('This is function')

@decorator
def f1(fun_name):
    print('This is function name:', fun_name)

@decorator
def f2(fun_name1, fun_name2):
    print('This is function name:', fun_name1)
    print('This is function name:', fun_name2)

@decorator
def f3(fun_name1, fun_name2, **para):
    print('This is function name:', fun_name1)
    print('This is function name:', fun_name2)
    print(para)

# f0()  # 不带参数
# f1('test_func')  # 带一个参数
# f2('x','y')  # 带两个参数
# f3('func_3', 'name_3', x=1, y=2)  # 关键字参数