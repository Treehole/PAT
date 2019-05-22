# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/22 23:47'

a = input().upper()
b = input().upper()
c = []

for i in a:
    if i not in b and i not in c:
        c.append(i)
print(''.join(c))