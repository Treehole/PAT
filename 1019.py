# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/10 22:37'

def minus(n):
    a = int(''.join(sorted(str(n).zfill(4), reverse=True)))
    b = int(''.join(sorted(str(n).zfill(4))))
    return a, b, a-b
n = int(input())
a, b, result = minus(n)
if result==0:
    print('{0} - {0} = 0000'.format(str(n)))
else:
    while True:
        a, b, result = minus(n)
        print('{0} - {1} = {2}'.format(str(a).zfill(4), str(b).zfill(4), str(result).zfill(4)))
        n = result
        if result == 6174:
            break