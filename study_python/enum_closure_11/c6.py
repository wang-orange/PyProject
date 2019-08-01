
# 使用非闭包实现功能：起点为0，每走一步增加1，走3步，当前位置为3，再走5步，位置为8
origin = 0
def go(step):
    global origin
    # nonlocal origin  # 为何会报错？？？？
    new_pos = origin + step
    origin = new_pos
    return origin

# 使用闭包实现
ori = 0
def tour(pos):
    def go(step):
        nonlocal pos  # 声明pos不是局部变量
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go

print(go(3))
print(go(5))
print('------------------')
f = tour(ori)
print(f(3))
print(f(5))
