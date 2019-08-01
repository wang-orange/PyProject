# re.sub 字符串替换

import re

language = 'pythonC#javaPHPC#'
r = re.sub('C#', 'GO', language, count=1)
print(r)
# lan = language.replace('C#', 'GO')
# print(lan)

# 将函数作为待替换的参数
def convert(value):
    print(value)
    matched = value.group()
    return '--' + matched + '--' 

r = re.sub('C#', convert, language)
print(r)