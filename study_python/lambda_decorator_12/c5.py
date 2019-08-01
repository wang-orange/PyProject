from functools import reduce

# reduce
# 连续计算，连续调用lambda
# lambda必须是两个参数
list_x = [1, 2, 3, 4, 5, 6, 7]
# ((((((1+2)+3)+4)+5)+6)+7)
r = reduce(lambda x,y: x+y, list_x) 
print(r)

list_x = ['1', '2', '3', '4', '5']
r = reduce(lambda x,y:x+y, list_x, 'abc')  # 以'abc'为初始值
print(r)
