# 列表推导式
# 集合推导式
# map filter
# set、dict、tuple也可以被推导

import array

a =  [i for i in range(10)]

# 需求1：a中元素的平方得到的新列表

# 用map实现 
b = map(lambda x: x*x, a)
print(list(b))

# 用列表推导式实现
c = [i*i for i in a]
print(c)

# 需求2：列表中的元素大于等于5时，对其平方，组成新列表
print('--------------------')

# map实现
# 先用filter过滤一下
e = filter(lambda x: x>=5, a)  
e = map(lambda x: x**2, list(e))
print(list(e))

# 列表推导式
d = [i**2 for i in a if i>=5]  
print(d)

# 集合被推导
set = {i**2 for i in range(5)}
print(set)

