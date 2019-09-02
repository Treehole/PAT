# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/26 0:49'

import re

string = input()
sum = 0
string = re.sub('[^a-zA-Z]', '', string).lower()
for char in string:
    sum += ord(char)-96
print(sum)
erjinzhi = str(bin(sum)[2:])
print(erjinzhi)
print(erjinzhi.count('0'), erjinzhi.count('1'))
