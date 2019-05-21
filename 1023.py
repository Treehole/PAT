# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/21 23:24'

a = input().split()
a = [int(i) for i in a]
result = ''
for i in range(1, 10):
    result += str(i)*a[i]
if a[0] != 0:
    result = result[0] + '0'*a[0] + result[1:]
print(result)