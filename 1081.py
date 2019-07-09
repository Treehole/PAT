# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/9 22:15'

import re


counts= int(input())
for i in range(counts):
    password = input()
    if len(password) < 6:
        print('Your password is tai duan le.')
    else:
        normal = re.findall('[a-zA-Z0-9\.]', password)
        zimu = re.findall('[a-zA-Z]', password)
        shuzi = re.findall('[0-9]', password)
        if len(normal) != len(password):
            print('Your password is tai luan le.')
        elif len(zimu) == 0:
            print('Your password needs zi mu.')
        elif len(shuzi) == 0:
            print('Your password needs shu zi.')
        else:
            print('Your password is wan mei.')
