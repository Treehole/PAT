# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 21:14'

student_num = int(input())
mingzis = []
xuehaos = []
chengjis = []
for i in range(student_num):
    mingzi, xuehao, chengji = input().split()
    mingzis.append(mingzi)
    xuehaos.append(xuehao)
    chengjis.append(int(chengji))
max_num = max(chengjis)
min_num = min(chengjis)
max_index = chengjis.index(max_num)
min_index = chengjis.index(min_num)
print(mingzis[max_index] + ' ' + xuehaos[max_index] + '\n' + mingzis[min_index] + ' ' + xuehaos[min_index])