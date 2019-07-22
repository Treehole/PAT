# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/22 22:33'

import re

sub_str = input()
start_str = input()
for i in sub_str:
    if i.isalpha():
        start_str = start_str.replace(i, '')
        start_str = start_str.replace(i.lower(), '')
    else:
        if i != '+':
            start_str = start_str.replace(i, '')
        else:
            start_str = re.sub('[A-Z]', '', start_str)
print(start_str)