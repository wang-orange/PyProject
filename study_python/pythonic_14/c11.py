# 装饰器的副作用
# 加了装饰器以后，会改变原函数的名字
# 为了不改变原函数的名字，需要引入wraps

import time
from functools import wraps

def decorator(func):
    @wraps(func)  # 加装饰器wraps后，原函数func的名字就不会被更改了
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decorator
def f1():
    '''
        This is f1
    '''
    print(f1.__name__)

f1()
help(f1)