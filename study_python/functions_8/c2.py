# 优先使用局部变量
# 作用域链，逐级寻找变量
c = 1

def func1():
    # c = 2
    def func2():
        # c = 3
        print(c)
    func2()

func1()