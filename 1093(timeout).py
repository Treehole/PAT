# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/9/2 20:22'

str1 = input()
str2 = input()

result = []
for i in str1:
    if ord(i) not in result:
        result.append(ord(i))
for j in str2:
    if ord(j) not in result:
        result.append(ord(j))
str3 = list(map(chr, result))
print(''.join(str3))