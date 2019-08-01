# filter: 将元素作为参数逐个传给函数，返回结果为True的值
import re

list_x = [1, 0, 3, 2, 0, 4]
# 过滤掉0
r = filter(lambda x: x, list_x)
print(list(r))

list_u = ['a', 'B', 'A', 'c'] 
# 保留小写字母
r = filter(lambda x: re.findall('[^A-Z]', x), list_u)
print(list(r))
