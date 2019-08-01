# re.match 从字符串开头开始匹配，没有找到，返回None，否则，返回第一个
# re.search 尝试搜索整个字符串，直到找到满足条件的第一个，并返回

import re

s = '123kjkj24jk95kl6'
r = re.match('\d', s)
print(r)
r1 = re.search('\d', s)
print(r1)
r2 = re.findall('\d', s)
print(r2)