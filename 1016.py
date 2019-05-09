# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/9 22:35'

a, da, b, db = input().split()
count_a = a.count(da)
count_b = b.count(db)
pa = da*count_a if count_a != 0 else '0'
pb = db*count_b if count_b != 0 else '0'
pa = int(pa)
pb = int(pb)
print(pa+pb)