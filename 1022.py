# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/21 22:55'

a, b, d = input().split()
c = int(a) + int(b)

def transfer(number, jz, new_number=''):
    if number >= jz:
        result = number//jz
        new_number += str(number-result*jz)
        transfer(result, jz, new_number)
    else:
        new_number += str(number)
        print(new_number[::-1])
transfer(c, int(d))
