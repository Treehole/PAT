# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/21 0:26'

n = int(input())
jia = 0
yi = 0
for i in range(n):
    a, b, c, d = input().split()
    he = str(int(a) + int(c))
    if he == b and he != d:
        yi += 1
    elif he != b and he == d:
        jia += 1
print('%s %s' % (str(jia), str(yi)))
