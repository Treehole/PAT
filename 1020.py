# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/10 23:07'

from operator import itemgetter

zl, xql = input().split()
kc = [int(i) for i in input().split()]
sj = [int(i) for i in input().split()]
jj = []
for i in range(int(zl)):
    jj.append([kc[i], kc[i]/sj[i]])
new_jj = sorted(jj, key=itemgetter(1), reverse=True)
for i in n