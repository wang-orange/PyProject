# bool 与if 之间的关系
# if判断时，存在不一定是True

class Test():
    def __len__(self):
        return 0
    def __bool__(self):
        return True
    # pass

test = Test()
if test:
    print('s')
else:
    print('F')
 
print(bool(test))
print(bool([]))
print(bool(None))