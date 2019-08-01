import copy

# 浅拷贝、深拷贝

l1 = [11, 12]
l2 = [21, 22]
num = 555

orgi = [l1, l2, num]

nList = orgi[:]  # 浅拷贝
deep = copy.deepcopy(orgi)  # 深拷贝

print("orgi:"+str(id(orgi)))
print("orgi[0]:"+str(id(orgi[0])))
print("orgi[1]:"+str(id(orgi[1])))
print("orgi[2]:"+str(id(orgi[2])))
print("*"*30)
print("nList:"+str(id(nList)))
print("nList[0]:"+str(id(nList[0])))
print("nList[1]:"+str(id(nList[1])))
print("nList[2]:"+str(id(nList[2])))
print('*'*30)
orgi[0][0] = 33
print(nList[0][0])
print('*'*30)
print("deep:"+str(id(deep)))
print("deep[0]:"+str(id(deep[0])))
print("deep[1]:"+str(id(deep[1])))
print("deep[2]:"+str(id(deep[2])))
print(deep[0][0])

