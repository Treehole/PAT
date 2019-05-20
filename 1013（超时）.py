# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/15 22:21'

import math

def sushu(x):
	a = math.sqrt(x)
	b = math.floor(a)
	for i in range(2,int(b + 1)):
		if(x % i == 0):
			a = 0
			break
	if a == 0:
		return False
	return True
sushus = [2]
i = 3
start, end = input().split()
while len(sushus) < int(end):
	if sushu(i):
		sushus.append(i)
	i += 1
new_sushus = [str(i) for i in sushus]
for i in range(int(start)-1, len(sushus), 10):
	print(' '.join(new_sushus[i:i+10]))