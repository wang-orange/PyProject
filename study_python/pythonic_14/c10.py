# 触发调用__len__()函数的两种方式
# len()
# bool()

class Test():
    def __len__(self):
        # return '8'
        # return 1.0
        return True  # 必须是整型或者bool类型
    def __bool__(self):
        # return 1  # 报错
        return True  # 必须是bool类型
    # pass

# 如果没有函数__len__()，调用内置函数len()将报错
print(len(Test()))  
print(bool(Test()))