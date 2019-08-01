import re

# 从字符串中找到数字
a = 'C0C++3Java4C#5python6JavaScript9123python'

r = re.findall('\d', a)
print(r)

