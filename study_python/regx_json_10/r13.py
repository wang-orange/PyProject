# 序列化

import json

student = [
    {"name":"zhangying", "age":18, "flag":False}, 
    {"name":"lisi", "age":18, "flag":None}
]

json_str = json.dumps(student)
print(type(json_str))
print(json_str)