from enum import Enum
from enum import IntEnum, unique

@unique  # 枚举变量不允许重复
class VIP(IntEnum):
    YELLOW = 1
    BLUE = 1  # 会报错
    RED = 3
    GREEN = 4
