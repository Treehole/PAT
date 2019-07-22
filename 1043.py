# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/22 23:04'

string = input()
new_string = ''
p_count = string.count('P')
a_count = string.count('A')
t_count = string.count('T')
e_count = string.count('e')
s_count = string.count('s')
low_t_count = string.count('t')

for i in range(max(p_count, a_count, t_count, e_count, s_count, low_t_count)):
    if p_count > 0:
        new_string += 'P'
        p_count -= 1
    if a_count > 0:
        new_string += 'A'
        a_count -= 1
    if t_count > 0:
        new_string += 'T'
        t_count -= 1
    if e_count > 0:
        new_string += 'e'
        e_count -= 1
    if s_count > 0:
        new_string += 's'
        s_count -= 1
    if low_t_count > 0:
        new_string += 't'
        low_t_count -= 1
print(new_string)