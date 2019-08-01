# 把函数作为参数传递

import re

s = 'AB12sf6kd9j3jl7'

# 将字符串中大于等于6的数字替换成9，小于6的替换成0
def convert(value):
    matched = value.group()
    if matched >= '6':
        return '9'
    else:
        return '0'

r = re.sub('\d', convert, s)
print(r)