# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/9/2 19:58'

import math
def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

length1, length2 = input().split()
num = input()
for i in range(int(length1)-int(length2)+1):
    new_num = num[i:i+int(length2)]
    if isPrime(int(new_num)):
        print(new_num)
        break
else:
    print('404')