# map配合lambda使用
'''
1.lambda中有几个参数，map就应该带几个列表
2.结果中元素个数取决于列表中个数少的
'''

# list_x = [1, 2, 3, 4, 5, 6, 7]
list_x = [1, 2, 3, 4, 5]
list_y = [1, 4, 9, 16, 25, 36, 49]
# list_y = [1, 4, 9, 16, 25]

r = map(lambda x, y: x*x + y, list_x, list_y)  # 将list_x、list_y中元素逐个传入函数square中进行计算，将结果保存在map中
print(list(r))

