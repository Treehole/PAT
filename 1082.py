# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/26 22:02'

counts = int(input())
results = {}
for i in range(counts):
    scores = input().split()
    a = int(scores[1])
    b = int(scores[2])
    results[scores[0]] = a*a + b*b
results = sorted(results,key=results.__getitem__)
print(results[0], results[-1])