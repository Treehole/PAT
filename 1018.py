# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/9 22:51'

r_a = [0, 0, 0]
r_b = [0, 0, 0]
w_a = []
w_b = []
def get_result(a, b):
    if a == b:
        r_a[1] += 1
        r_b[1] += 1
    elif a=='B' and b=='J':
        w_b.append('J')
        r_a[2] += 1
        r_b[0] += 1
    elif a=='J' and b=='C':
        w_b.append('C')
        r_a[2] += 1
        r_b[0] += 1
    elif a=='C' and b=='B':
        w_b.append('B')
        r_a[2] += 1
        r_b[0] += 1
    elif a=='B' and b=='C':
        w_a.append('B')
        r_a[0] += 1
        r_b[2] += 1
    elif a=='J' and b=='B':
        w_a.append('J')
        r_a[0] += 1
        r_b[2] += 1
    elif a=='C' and b=='J':
        w_a.append('C')
        r_a[0] += 1
        r_b[2] += 1
num = int(input())
for i in range(num):
    a, b = input().split()
    get_result(a, b)
def max_w(l):
    max_c = 'B'
    count_c = l.count('C')
    count_b = l.count('B')
    count_j = l.count('J')
    if count_c > count_b:
        max_c = 'C'
        if count_j > count_c:
            max_c = 'J'
    elif count_j > count_b:
        max_c = 'J'
    return max_c

m_a = max_w(w_a)
m_b = max_w(w_b)
print(' '.join([str(i) for i in r_a]))
print(' '.join([str(i) for i in r_b]))
print('%s %s' % (m_a, m_b))