# 正则表达式：是一个特殊的字符序列，查找一个字符串是否与我们所设定的字符序列想匹配

'''
使用场景，比如：
1.检查一串字符串是否为电话号码
2.检测一个字符串是否符合email
3.把一个文本里的指定单词替换为另一个单词
'''
import re

a = 'C0C++3Java4C#5python6JavaScript9123python'
res = re.findall('python', a)
print(res)



