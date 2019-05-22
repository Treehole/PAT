# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/22 22:24'

n, fuhao = input().split()
for i in range(1, 1000, 2):
    total = (i+1)*(i+1)/2 - 1
    if int(n) < total:
        m = i-2
        break
for i in range(m, 0, -2):
    j = int((m - i)/2)
    print(' '*j + fuhao*i)
for i in range(3, m+1, 2):
    j = int((m - i)/2)
    print(' ' * j + fuhao * i)
print(int(n) - int((m+1)*(m+1)/2-1))