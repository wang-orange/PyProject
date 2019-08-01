import os,sys
cwd = os.getcwd()
dir = os.path.dirname(cwd)
sys.path.append(dir)
# print(sys.path)
# from package_module.c1 import *
# from test import t2
from package_module_7 import *
import test

print(c1.a)
print(c2.e)

# print(a)
# print(c)
# # print(b)
# print(t2.b)