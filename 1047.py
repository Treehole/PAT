# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/26 0:33'

count = int(input())
scores = {}
for i in range(count):
    a = input().split()
    b = a[0].split('-')
    if b[0] not in scores:
        scores[b[0]] = int(a[1])
    else:
        scores[b[0]] += int(a[1])
for k in sorted(scores, key=scores.__getitem__, reverse=True):
    print(k, scores[k])
    break