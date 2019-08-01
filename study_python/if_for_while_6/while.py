# 递归时用while更适合
counter = 1
while counter < 20:
    print(counter)
    counter+=1
else:
    print('EOF')

# for i in range(20):
#     print(counter)
#     counter += 1
#     if counter > 19:
#         print('EOF')
#         break