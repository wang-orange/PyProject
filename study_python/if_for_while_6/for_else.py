# 主要用于遍历/循环 序列或者集合、字典
a = [['apple','orange','banana'],(1,2,3)]
for x in a:
    for y in x:
        if y == 'orange':
            break # 跳出本次循环
        print(y)
else:
    print('Over--')

# b = [1,2,3,4,5]
# for x in b:
#     if x == 3:
#         break
#         # continue
#     print(x)
# else: # for正常结束后才能执行该语句
#     print('EOF')