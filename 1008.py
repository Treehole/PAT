# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 21:31'

N, M = input().split()
chushi = input().split()
cha = int(N) - int(M)
result = chushi[cha:]
result.extend(chushi[:cha])
print(' '.join(result))