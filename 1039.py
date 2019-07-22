# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/22 22:50'


tanzhu = list(input())
xiaohong = input()
queshao = 0

for i in xiaohong:
    if i in tanzhu:
        tanzhu.remove(i)
    else:
        queshao += 1
if queshao != 0:
    print('No', queshao)
else:
    print('Yes', len(tanzhu))