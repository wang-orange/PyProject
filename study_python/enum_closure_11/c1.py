# 类型
# 枚举 enum
# 1.变量不可更改
# 2.防止出现相同标签

from enum import Enum

class VIP(Enum):
    YELLOW = 1
    # YELLOW = 5  # 不可定义相同标签
    YELLOW_ALIAS = 1  # 第二个数值相同的是第一个的“别名”
    BLUE = 2
    RED = 3
    GREEN = 4

class Common():
    YELLOW = 1
    YELLOW = 5

# 遍历
# for i in VIP:
#     print(i.name)  # 别名的不会输出
# print('-----------------')
# for i in VIP.__members__:  # 遍历所有的成员，包括别名
#     print(i)
# print('-----------------')
# for i in VIP.__members__.items():
#     print(i)

# print(VIP.YELLOW)  
# print(VIP.YELLOW.name)  # 枚举的名字str
# print(VIP.YELLOW.value)  # 枚举的值
# print(type(VIP.YELLOW))
# print(type(VIP.YELLOW.name))
print(VIP['YELLOW'])
print(Common.YELLOW)
print(VIP.BLUE)
VIP.YELLOW = 5  # 改值报错
Common.YELLOW = 5 