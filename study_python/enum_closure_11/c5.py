
def f1():
    a = 10
    def f2():
        a = 20
        print('------->1: '+str(a))
    print('------->2: '+str(a))
    f2()
    print('------->3: '+str(a))

f1()