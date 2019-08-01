for i in range(0,10,2):
    print(i,end=' | ')
print('\n')

for i in range(10,0,-2):
    print(i,end=' | ')
print('\n')

a = [1,2,3,4,5,6,7,8]
for i in range(1,len(a),2):
    print(i, end=' | ')

b = a[len(a):0:-2]
print(b)