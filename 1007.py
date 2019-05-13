# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 21:15'

import math
def sushu(x):
	a = math.sqrt(x)
	b = math.floor(a)
	for i in range(2, b+1):
		if(x % i == 0):
			a = 0
			break
	if a == 0:
		return False
	return True
number = 0
j = 3
num_max = eval(input())
for i in range(3,num_max + 1,2):
	if sushu(i):
		if i - j == 2:
			number += 1
		j = i
print(number)