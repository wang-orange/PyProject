# 闭包 = 函数 + 环境变量(函数定义时)

def curve_pre():
    a = 25
    def curve(x):
        return a*x*x
    return curve

a = 10
f = curve_pre()
print(f(2))
print(f.__closure__)
print(f.__closure__[0].cell_contents)