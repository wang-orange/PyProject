# 空字符串、空列表、Flase、0
# None 不同于以上对象，无论是类型还是值上

a = None
b = ''
c = []
d = False

# 值比较
print(a == b)
print(a == c)
print(a == d)
print(a == 0)

# <class 'NoneType'>
print(type(a))
print(type(b))