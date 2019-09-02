# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/30 21:54'

mooncake, city = input().split()
total = [0]*int(mooncake)
for i in range(int(city)):
    sale = list(map(int, input().split()))
    for j in range(int(mooncake)):
        total[j] += sale[j]
max_sale = max(total)
max_sale_index = []
for k, l in enumerate(total):
    if l==max_sale:
        max_sale_index.append(str(k+1))
print(max_sale)
print(' '.join(max_sale_index))