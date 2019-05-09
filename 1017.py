# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/9 22:45'

a, b = input().split()
q = int(a) // int(b)
r = int(a) - q * int(b)
print('%s %s' % (str(q), str(r)))