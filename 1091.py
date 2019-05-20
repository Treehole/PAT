# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/20 23:27'

m = input()
numbers = input().split()
for i in numbers:
    square = int(i)**2
    for j in range(1, 10):
        result = str(square*j)
        if result.endswith(i):
            print('%s %s' % (str(j), result))
            break
    else:
        print('No')