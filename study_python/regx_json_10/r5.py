# 边界匹配
# ^ 以^后的字符开头
# $ 以$前的字符结尾

import re

qq = '10000000'
# 匹配整个字符串是否是 4~8 位的数字
# r = re.findall('\d{4,8}', qq)
r = re.findall('^\d{4,8}$', qq)
print(r)

