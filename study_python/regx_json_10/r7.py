# 匹配模式参数
# re.I 忽略大小写
# re.S 使. 匹配包括换行符在内的所有字符

import re

a = 'python22C#\nPHP'
r = re.findall('c#.{1}', a, re.I | re.S)
print(r)

