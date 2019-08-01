# 类与对象
# 类变量：与类关联在一起
# 实例变量：与对象关联在一起

class Student():
    name = 'yiyue'  
    age = 0
    # 一个班级的总人数
    sum = 0  # 类变量
    
    def __init__(self, name, age):
        # 构造函数：初始化对象的属性
        self.name = name  # 使用self定义实例变量
        self.age = age
    
    # 行为与特征（属性）
    def do_homework(self):
        print('homework')

student1 = Student('石敢当', 18)
student2 = Student('喜小乐', 20)
print(student1.name) 
print(student2.name)
print(Student.name)


