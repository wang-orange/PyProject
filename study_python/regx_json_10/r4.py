# 数量词 {m, n}
# 贪婪 与 非贪婪（? 针对范围时）
# * 匹配*前的字符0次或无限次 [0,)
# + 匹配+前的字符1次或无限次[1,)
# ? 匹配?前的字符0次或1次[0,1]

import re

s = 'python 2111java678php'
# 默认贪婪匹配
r = re.findall('[a-z]{3,6}', s)
print(r)

# 非贪婪?
print('----------非贪婪')
r = re.findall('[a-z]{3,6}?', s)
print(r)

s = 'pytho123python1pythonn2'
print('----------*')
r = re.findall('python*', s)
print(r)

print('----------+')
r = re.findall('python+', s)
print(r)

print('----------?')
r = re.findall('python?', s)
print(r)

