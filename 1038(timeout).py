# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/25 21:04'

students_count = int(input())
scores = input().split()
chaxun = input().split()
result = {}
results = []
for j in chaxun[1:]:
    result[j]=0
for i in scores:
    if i in chaxun[1:]:
        result[i] += 1
for k in result.keys():
    results.append(str(result[k]))
print(' '.join(results))