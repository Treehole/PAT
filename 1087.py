# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/9/2 21:41'


num = int(input())
result = set()
for i in range(1, num+1):
    result.add(int(i/2) + int(i/3) + int(i/5))
print(len(result))