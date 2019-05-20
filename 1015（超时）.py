# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/20 22:01'

import functools

def cmpf(a, b):
    if a[3] != b[3]:
        return -1 if b[3]>a[3] else 1
    elif a[1] != b[1]:
        return -1 if b[1] > a[1] else 1
    else:
        return -1 if int(a[0]) > int(b[0]) else 1

n, l, h = input().split()
l = int(l)
h = int(h)
first_class = []
second_class = []
third_class = []
forth_class = []
for i in range(int(n)):
    examination_number, de_score, cai_score = input().split()
    de_score = int(de_score)
    cai_score = int(cai_score)
    sum_score = de_score + cai_score
    if de_score < l or cai_score <l:
        continue
    elif de_score >= h and cai_score >= h:
        first_class.append([examination_number, de_score, cai_score, sum_score])
    elif de_score >=h and cai_score >= l:
        second_class.append([examination_number, de_score, cai_score, sum_score])
    elif de_score >=l and cai_score >=l and de_score>=cai_score:
        third_class.append([examination_number, de_score, cai_score, sum_score])
    elif de_score >=l and cai_score >=l:
        forth_class.append([examination_number, de_score, cai_score, sum_score])
decai_counts = len(first_class) + len(second_class) + len(third_class) +len(forth_class)
print(decai_counts)
for i in [first_class, second_class, third_class, forth_class]:
    i = sorted(i, key=functools.cmp_to_key(cmpf), reverse=True)
    for j in i:
        print('{0} {1} {2}'.format(j[0], j[1], j[2]))