obj = [2, 3 , 5 , 7, 9]
for i in obj:    # for and in is keyword,  i is itterate, obj is which one need to itterate
    print(i)

print('Adding*******************')
for i in obj:
    print(i+2)

print('Range*******************')
for j in range(1, 6):
    print(j)

print('Sum of first natural no.*******************') #1+2+3+4 = 10
Summation = 0
for i in range(1, 6):
    Summation = Summation + i
    print(Summation)

print('This syntex is jump with specific itteration count*******************')
for K in range(1, 15, 5):
    print(K)

print('This syntex for only upper count*******************')
for m in range(10):
    print(m)

