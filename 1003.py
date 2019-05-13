# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 20:17'

import re

num = int(input())
for i in range(num):
    string = input()
    if string == 'PAT':
        print('YES')
    else:
        try:
            a = re.match('(.*?)P', string).group(1)
            b = re.match('.*?P(.*?)T', string).group(1)
            c = re.match('.*?P.*?T(.*)', string).group(1)
            if a == '' and c == '' and set(b) == {'A'}:
                print('YES')
            elif set(a) != {'A'}:
                print('NO')
            elif set(b) != {'A'}:
                print('NO')
            elif set(c) != {'A'}:
                print('NO')
            elif a.count('A')*b.count('A') != c.count('A'):
                print('NO')
            else:
                print('YES')
        except:
            print('NO')