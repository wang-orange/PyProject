# 子类
from c6 import Human

class Student(Human):
    
    def __init__(self, school, name, age):
        self.school = school
        # Human.__init__(self, name, age)
        super(Student, self).__init__(name, age)

    def do_homework(self):
        super(Student, self).do_homework()  # 调用父类的方法
        print('homework')

student1 = Student('人民路小学', '石敢当', 18)
student1.do_homework()
# print(student1.school)
# print(student1.age)
# student1.get_name()
