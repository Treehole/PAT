# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/22 22:16'

sum_numbers = []
numbers = input().split()[1:]
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            sum_numbers.append(int(numbers[i] + numbers[j]))
print(sum(sum_numbers))