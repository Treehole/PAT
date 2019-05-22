# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/22 23:52'

n = int(input())
results = {}
for i in range(n):
    serial, result = input().split()
    if serial in results.keys():
        results[serial] += int(result)
    else:
        results[serial] = int(result)
new_results = sorted(results.items(), key=lambda d:d[1], reverse = True)
print('%s %s' % (new_results[0][0], str(new_results[0][1])))