# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/21 23:40'

number = input()
fuhao = number[0]
a, b = number[1:].split('E')
zero_counts = 0
a = list(a)
if int(b) >= 0:
    for i in range(int(b)):
        index = a.index('.')
        if a[-1] != '.':
            a[index], a[index+1] = a[index+1], a[index]
        else:
            a[-1] = '0'
            a.append('.')
    if a[-1]=='.':
        a = a[:-1]
        result = ''.join(a)
    else:
        result = ''.join(a)
else:
    for i in range(0, int(b), -1):
        index = a.index('.')
        if a[1] != '.':
            a[index], a[index-1] = a[index-1], a[index]
        else:
            a = ['0'] + a
            a[1], a[2] = a[2], a[1]
    result = ''.join(a)
if fuhao == '-':
    result = '-' + result
print(result)