# 类与对象的变量的查找顺序:
# 先从实例变量中查找，没有，再从类变量中找，没有，再从父类中找

class Student():
    name = 'yiyue'  # 类变量
    age = 0
    
    def __init__(self, name, age):
        name = name  
        age = age
         
    # 行为与特征（属性）
    def do_homework(self):
        print('homework')

student = Student('石敢当', 18)
print(student.__dict__)
# print(Student.__dict__)
print(student.name)  # 为何打印的结果为‘yiyue’ ？ 因为实例变量中没有name，最后取了类变量name