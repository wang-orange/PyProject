# 枚举转换
from enum import Enum

class VIP(Enum):
    YELLOW = 1
    BLUE = 2
    RED = 3
    GREEN = 4

a = 1
print(VIP(a))  # 值与枚举类型对应