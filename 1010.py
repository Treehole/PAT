# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 21:31'

numbers = input().split()
new_numbers = []
if numbers[1] == '0':
    new_numbers = ['0', '0']
else:
    for i in range(0, len(numbers), 2):
        if int(numbers[i+1]) > 0:
            new_numbers.append(str(int(numbers[i])*int(numbers[i+1])))
            new_numbers.append(str(int(numbers[i+1])-1))
print(' '.join(new_numbers))