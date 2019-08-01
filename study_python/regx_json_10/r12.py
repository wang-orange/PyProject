# Json
import json
'''
json的数据格式到python的对应转换：
json    python
object  dict
array   list
string  str
number  int
number  float
true    True
flase   Flase
null    None
'''

print("\n-------- JSON objec -------")
json_str = '{"name":"zhangying", "age":18}'  # json字符串里必须用双引号
# json_str = "{'name':'zhangying', 'age':18}"  # 报错
# 反序列化
student = json.loads(json_str)  # 转换成python对象-字典
print(type(student))
print(student)
print(student['name'])

print("\n-------- JSON array -------")
json_arr = '[{"name":"zhangying", "age":18, "flag":false}, {"name":"lisi", "age":18, "flag":null}]'
student = json.loads(json_arr)
print(type(student))
print(student)