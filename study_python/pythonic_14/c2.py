# 对应c1.py，用字典模拟

day = 5

def get_sunday():
    return 'Sunday'

def get_monday():
    return 'Monday'

def get_tuesday():
    return 'Tuesday'

def get_default():
    return 'Unknown'

switcher = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuseday'
}

# value也可以为函数 
switcher1 = {
    0: get_sunday,  
    1: get_monday,
    2: get_tuesday
}

day_name = switcher.get(day, 'Unknown')

# 用get方法获取字典的元素
day_name = switcher1.get(day, get_default)() 
print(day_name)

