# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/10 23:07'

from operator import itemgetter

zl, xql = input().split()
xql = float(xql)
kc = [float(i) for i in input().split()]
sj = [float(i) for i in input().split()]
jj = []
for i in range(int(zl)):
    jj.append([kc[i], sj[i]/kc[i]])
new_jj = sorted(jj, key=itemgetter(1), reverse=True)
zsj = 0
for i in new_jj:
    if xql >= i[0]:
        zsj = zsj + i[0]*i[1]
        xql = xql - i[0]
    else:
        zsj = zsj + xql*i[1]
        break
print('%.2f' % zsj)