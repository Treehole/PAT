# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 20:16'

num = int(input())
n = 0
while num != 1:
    if num % 2 == 0:
        num = num / 2
        n = n + 1
    else:
        num = (num * 3 + 1) / 2
        n = n + 1
print(n)