# 作用域
c = 10  # 全局变量
def demo():
    c = 50  # 局部变量
    # python中没有“块级作用域”，像if/else、for、while中的变量不可能形成块级的作用域，其变量和函数同级别
    for i in range(9):
        c += 1
        a = 'a'
    print(c)
    print(a)

demo()
