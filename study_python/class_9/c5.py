# 9-12 成员可见性：公开和私有

class Student():

    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__score = 0  # 变量名前加双下滑线，将公有变私有
    
    def marking(self, score):
        if score < 0:
            return '不能给别人打负分！'
        self.__score = score
        return (self.name + '同学本次考试的分数为：' + str(self.__score))
    

student = Student('石敢当', 20)
# print(student.__score)  # 外部不能直接访问私有变量
print(student.__dict__)  # 查看对象的成员列表，可以看到私有变量score的名称被该为_Student__score
print(student._Student__score)  # 可以通过改后的私有变量名来访问私有变量
student.__score = 67  # 这里没有报错，并不是访问了私有变量score，而是添加了一个实例变量score
print(student.__dict__)  # 再次查看成员列表
