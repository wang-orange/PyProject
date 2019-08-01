# 实例方法：定义时需携带参数self，代表对象本身
# 类方法：在方法前添加装饰器@classmethod，定义时需携带参数cls，代表类本身
# 静态方法：在方法前加装饰器@staticmethod

class Student():
    # 一个班级的总人数
    sum = 0  # 类变量
    
    def __init__(self, name, age):
        # print(self)
        self.name = name  # 实例变量
        self.age = age
    
    # 行为与特征（属性）
    def do_homework(self):
        self.homework_name = 'English'
        print('homework')

    def do_english_homework(self):
        self.do_homework()
        print(self.homework_name)  # 实例方法可以相互访问对方的变量

    # 类方法
    @classmethod
    def plus_sum(cls):  # 和self一样，cls也可以叫其他的名字
        # print(cls)
        cls.sum += 1
        print("班级当前的总人数：" + str(cls.sum))
        # print(student.name)  # 不能在类方法中调用实例变量
    
    # 静态方法
    @staticmethod
    def add():
        Student.sum += 1
        print(Student.sum)  # 静态方法访问类变量
        print("This is static function")
        # print(self.name)  # 不能在静态方法中调用实例变量


student1 = Student('石敢当', 18)
# student1.do_english_homework()
# Student.do_english_homework()   # 实例方法只能由对象来调用，类不可以访问
# Student.plus_sum()  # 通过类调用类方法
# student1.plus_sum()  # 通过对象调用类方法
# student2 = Student('喜小乐', 20)
# Student.plus_sum()
# print(Student.sum)
# student1.add()
Student.add()