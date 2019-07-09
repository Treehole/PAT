# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/9 22:39'

counts = int(input())
password = ''
duizhao = {
    'A': '1',
    'B': '2',
    'C': '3',
    'D': '4'
}
for i in range(counts):
    options = input()
    for j in options.split():
        if j[2] == 'T':
            password += duizhao[j[0]]
print(password)