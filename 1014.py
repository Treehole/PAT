# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/16 22:27'

import re
a = input()
b = input()
c = input()
d = input()
day = {'A':'MON', 'B': 'TUE', 'C': 'WED', 'D': 'THU', 'E': 'FRI', 'F': 'SAT',
       'G': 'SUN'}
hour = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F':'15',
        'G': '16', 'H': '17', 'I':'18', 'J': '19', 'K':'20', 'L':'21',
        'M':'22', 'N': '23'}

try:
    same_letters = []
    for i, letter in enumerate(a):
        if letter == b[i]:
            same_letters.append(letter)
except:
    pass
for letter in same_letters:
    if letter in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        final_day = letter
        break
for letter in same_letters[same_letters.index(final_day)+1:]:
    if letter in hour.keys():
        final_hour = hour[letter]
        break
    elif letter in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        final_hour = letter.zfill(2)
        break
try:
    for i, letter in enumerate(c):
        if letter == d[i] and letter.isalpha():
            minute = i
            break
except:
    pass
final_day = day[final_day]
final_minute = str(minute).zfill(2)
print('%s %s:%s' % (final_day, final_hour, final_minute))