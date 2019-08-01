# 字典推导式

students = {
    '石敢当': 18,
    '赵晓明': 22,
    '张三丰': 33
}

names = {value: key for key,value in students.items()}
print(names)

name_tuple = (key for key,value in students.items())
print(name_tuple)
for i in name_tuple:
    print(i)
