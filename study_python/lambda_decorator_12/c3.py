# map: x->y 的映射

def square(x):
    return x*x

list_x = [1, 2, 3, 4, 5, 6, 7]
#list_y = [1, 4, 9, 16, 25, 36, 49]

for i in list_x:
    square(i)

r = map(square, list_x)  # 将list_x中元素逐个传入函数square中进行计算，将结果保存在map中
print(list(r))

