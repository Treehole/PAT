# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 20:10'

number = input()
numbers = sorted(set(number))
for i in numbers:
    print('{0}:{1}'.format(i, number.count(i)))
