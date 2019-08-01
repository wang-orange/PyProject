# 装饰器
import time

def f1():
    print('This is function 1')

def f2():
    print('This is function 2')

# 遵循的原则：对修改时封闭的，对扩展时开放的
# 新需求：在每个函数中增加执行该函数时的当前时间
# 不改变原函数
def print_current_time(fun):
    print(time.time())
    fun()

# 这种实现，改变了原函数的调用方式
print_current_time(f1)  
print_current_time(f2)
