# 生成器 针对一个函数来说，迭代器是针对一个对象class来说
# print 0~10000


# 生成器，关键字yield
def gen(max):
    n = 0
    while n <= max:
        yield n
        n += 1

g = gen(10000)
# for i in g:
#     print(i)

# 元组推导式，结果是一个生成器
a = (i for i in range(10000))
print(a)
for i in a:
    print(i)




