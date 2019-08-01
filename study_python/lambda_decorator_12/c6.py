# 利用reduce 实现旅行位置计算
# pos：(x,y)表示位置
from functools import reduce

# (1,3) 表示在坐标轴中，向x正向走1步，向y正向走3步
go_list = [(1,3), (3,-4), (5,7)]

# 普通函数实现
def add(li):
    sum_x = 0
    sum_y = 0
    for i in go_list:
        sum_x += i[0]
        sum_y += i[1]
    return sum_x, sum_y

def reducer(x, y):
    print('x:', x)  
    print('y:', y)
    print('-------------')
    return x[0]+y[0], x[1]+y[1]

# 初始位置在(0,0)，计算按go_list走后的位置
r = reduce(lambda x,y: (x[0]+y[0], x[1]+y[1]), go_list)
# r = reduce(reducer, go_list, (0, 0))
print(r)
