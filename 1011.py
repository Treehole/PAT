# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 22:18'

nums = int(input())
results = []
for i in range(nums):
    a, b, c = input().split()
    if int(a) + int(b) > int(c):
        result = 'Case #%s: true' % str(i+1)
    else:
        result = 'Case #%s: false' % str(i + 1)
    results.append(result)
print('\n'.join(results))