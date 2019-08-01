# 带参数的装饰器

import time

def print_log(log):
    def decorator(fun):
        def wrapper(*args, **kw):
            print(time.time())
            fun(*args, **kw)
            print(log)
        return wrapper
    return decorator


@print_log('error------')
def f0():
    print('This is function')

f0()

# 不加装饰的调用
# f = print_log('error------')
# ff = f(f0)
# ff()