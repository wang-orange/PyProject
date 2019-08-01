from functools import reduce

scientists =({'name':'Alan Turing', 'age':105, 'gender':'male'},
             {'name':'Dennis Ritchie', 'age':76, 'gender':'male'},
             {'name':'Ada Lovelace', 'age':202, 'gender':'female'},
             {'name':'Frances E. Allen', 'age':84, 'gender':'male'})


# 需求：按性别分组

# 用for循环实现
gender_name = {'male': [], 'female': []}
for scientist in scientists:
    if scientist['gender'] == 'male':
        gender_name['male'].append(scientist['name'])
    else:
        gender_name['female'].append(scientist['name'])
print(gender_name)

print('----------------------')

# 用reduce实现
def group_by_gender(accumulator, scientist):
    accumulator[scientist['gender']].append(scientist['name'])
    return accumulator

grouped = reduce(group_by_gender, scientists, {'male': [], 'female': []})
print(grouped)
