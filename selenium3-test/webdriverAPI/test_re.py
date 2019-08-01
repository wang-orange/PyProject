# coding:utf-8
import re

'''
re.match(pattern, string, flags=0)
尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
args:
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等
'''
print(re.match('www','www.baidu.com').span())
print(re.match('com','www.baidu.com'))

print("1*********************************")
# match.group()
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
print(matchObj)

if matchObj:
    print("matchObj.group():", matchObj.group())
    print("matchObj.groups():", matchObj.groups())
    print("matchObj.group(1):", matchObj.group(1))
    print("matchObj.group(2):", matchObj.group(2))
else:
    print("No match")

print("2*******************************")
"""
re.search(pattern, string, flags=0) 扫描整个字符串并返回第一个成功的匹配。
args:
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""
print(re.search('www', 'www.baidu.com').span())
print(re.search('com', 'www.baidu.com').span())

print('3*******************************')
"""
re.sub(pattern, repl, string, count=0) 用于替换字符串中的匹配项。
args:
    pattern : 正则中的模式字符串。
    repl : 替换的字符串，也可为一个函数。
    string : 要被查找替换的原始字符串。
    count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
phone = "2004-978-1234 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*','',phone)
print(num)
# 删除非数字字符
num = re.sub(r'\D','',phone)
print(num)

print("4****************************")
'''
re.compile(pattern[, flags])
用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用

agrs:
    pattern : 一个字符串形式的正则表达式
    flags 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：
       re.I 忽略大小写
       re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
       re.M 多行模式
       re.S 即为' . '并且包括换行符在内的任意字符（' . '不包括换行符）
       re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
       re.X 为了增加可读性，忽略空格和' # '后面的注释
'''
pattern = re.compile(r'\d+')
m = pattern.match('one12twothree34four')
print(m)
m = pattern.match('one12twothree34four', 2, 10)
print(m)
m = pattern.match('one12twothree34four', 3, 10)
print(m)
print(m.group())
print(m.start())
print(m.end())
print(m.span())

print("5******************************************")
'''
findall(string[, pos[, endpos]])
在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
args:
    string 待匹配的字符串。
    pos 可选参数，指定字符串的起始位置，默认为 0。
    endpos 可选参数，指定字符串的结束位置，默认为字符串的长度。
'''
pattern = re.compile(r'\d+')
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
result3 = re.findall(r'\d+', 'run88oob123google456')
result4 = re.findall(r'run(\d+)', 'run88oob123google456')
print(result1)
print(result2)
print(result3)
print(result4)

print("6****************************************")
'''
re.finditer(pattern, string, flags=0)
和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回.
args:
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''
it = re.finditer(r'\d+', '12a32bc43jf3')
# print(it)
for match in it:
    print(match.group())

print("7*****************************************")
'''
re.split(pattern, string[, maxsplit=0, flags=0])
按照能够匹配的子串将字符串分割后返回列表
args:
    pattern	匹配的正则表达式
    string	要匹配的字符串。
    maxsplit	分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
    flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
'''
list = re.split(r'\W+', 'runoob, runoob, runoob')
print(list)
list = re.split(r'\W+', ' runoob, runoob, runoob.')
print(list)
list = re.split(r'\W+', ' runoob, runoob, runoob.', 1)
print(list)


