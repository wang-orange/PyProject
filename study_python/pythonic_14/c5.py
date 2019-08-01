# 列表、元组、集合、字典
# 可迭代对象 iterable
# 迭代器 iterator：
# 1)是对象 class
# 2)类中实现两个函数__iter__()、__next__()

# 浅拷贝、深拷贝

class BooksCollection():
    ''' 定义一个迭代器
    '''
    def __init__(self):
        self.data = ['《往事》', '《只能》', '《回味》']
        self.curor = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.curor >= len(self.data):
            raise StopIteration
        r = self.data[self.curor]
        self.curor += 1
        return r
    
books = BooksCollection()
import copy
# copy一个迭代器
books_copy = copy.copy(books)

# 可通过for循环访问迭代器
for i in books:
    print(i)

# 再次循环，将不输出
# 迭代器只能一次性访问
# for j in books:
#     print(j)

# 用next()访问
# print(next(books))
# print(next(books))
# print(next(books))

print('--------------')
for i in books_copy:
    print(i)

