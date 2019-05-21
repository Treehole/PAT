# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/21 23:40'

number = input()
fuhao = number[0]
a, b = number[1:].split('E')
zero_counts = 0
while a.endswith('0'):
    a = a[:-1]
    zero_counts += 1
result = float(a) * 10 ** int(b)
result = str(result) + '0'*zero_counts
if fuhao == '-':
    result = '-' + result
if result.endswith('.0'):
    result = result[:-2]
print(result)