# group 分组

import re
s = 'Life is short, I use python, i love python'

r = re.search('Life(.*)python(.*)python', s)
# print(r.group(0))
# print(r.group(1))
# print(r.group(2))
print(r.group(0, 1, 2))
print(r.groups())

# r1 = re.findall('Life(.*),(.*)python', s)
# print(r1)