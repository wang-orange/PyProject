# 实例方法：定义时固定传入参数self，调用时无需传入

class Student():
    name = 'yiyue'  # 类变量
    age = 0
    # 一个班级的总人数
    sum = 0  # 在实例方法中怎样访问类变量？ Student.sum
    
    def __init__(self, name, age):  # self可以改为其他名字
        # 构造函数：初始化对象的属性
        self.name = name  # 使用self定义实例变量
        self.age = age
        print(self.name)  # 打印的是实例变量
        # print(name)  # 打印的是形参name
        Student.sum += 1  # 在实例方法中访问类变量:Student.sum 或 self.__class__.sum
        print("班级当前学生总数：%d" %self.__class__.sum)
        # print(self.__class__.sum)
    
    # 行为与特征（属性）
    def do_homework(self):  # self代表对象，与类无关，谁调用了它，self就指代谁
        print('homework')
        # Student.sum = 3

student1 = Student('石敢当', 18)
# print(student1.__dict__)
student2 = Student('喜小乐', 20)
# print(student1.name) 
# print(student2.name)
# student1.print_info()
# print(Student.sum)