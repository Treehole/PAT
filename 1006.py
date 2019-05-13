# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 21:15'

num = int(input())
bai = num // 100
shi = (num - 100*bai) // 10
ge = num - 100*bai - 10*shi
print('B'*bai + 'S'*shi + '123456789'[:ge])