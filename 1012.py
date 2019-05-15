# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 22:54'


data_input = input().split()
list_a1 = []
list_a2 = []
list_a3 = []
list_a4 = []
list_a5 = []
a2 = 0
for i in range(int(data_input[0])):
    num = data_input[i+1]
    if num[-1] == '0':
        list_a1.append(int(num))
    elif num[-1] in ['1', '6']:
        list_a2.append(int(num))
    elif num[-1] in ['2', '7']:
        list_a3.append(num)
    elif num[-1] in ['3', '8']:
        list_a4.append(int(num))
    elif num[-1] in ['4', '9']:
        list_a5.append(int(num))
if list_a1:
    a1 = sum(list_a1)
else:
    a1 = 'N'
if list_a2:
    for i, j in enumerate(list_a2):
        a2 = a2 + (-1)**i*j
else:
    a2 = 'N'
if list_a3:
    a3 = len(list_a3)
else:
    a3 = 'N'
if list_a4:
    a4 = '%.1f' % (sum(list_a4)/len(list_a4))
else:
    a4 = 'N'
if list_a5:
    a5 = max(list_a5)
else:
    a5 = 'N'

print('{0} {1} {2} {3} {4}'.format(str(a1), str(a2), str(a3), a4, str(a5)))