# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/21 0:14'

a, b = input().split()
c = int(a) * int(b)
print(int(str(c)[::-1]))