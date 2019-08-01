# 组

import re

a = 'python pythonpythonpython'
r = re.findall('(python){3,5}', a)
print(r)