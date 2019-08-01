# 字符集 []  
# 概括字符集: 
# \d 数字 [0-9], \D 非数字 [^0-9], 
# \w 单词字符[A-Za-z0-9_]，\W 非单词字符
# \s 空白字符，\S 非空白字符
# . 匹配换行符\n之外的任意字符
# 只能匹配单一的字符

import re

print('-----------[]')
s = 'abc, acc, adc, aec, afc, ahc'
r = re.findall('a[fc]c', s)  # 普通字符用来定界，[fc]匹配f或c
print(r)

a = 'python 11\t22java&678p\nh__\rp'

print('-----------\d')
r = re.findall('\d', a)
print(r)

print('-----------\D')
r = re.findall('\D', a)
print(r)

print('-----------\w')
r= re.findall('\w', a)
print(r)

print('-----------\W')
r= re.findall('\W', a)
print(r)

print('-----------\s')
r= re.findall('\s', a)
print(r)

print('-----------\S')
r= re.findall('\S', a)
print(r)