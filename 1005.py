# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 21:15'

num_counts = int(input())
nums = input().split()
key_nums = []
not_key_nums = []
for num in nums:
    num = int(num)
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num * 3 + 1) / 2
        key_nums.append(str(int(num)))
for num in nums:
    if num not in key_nums:
        not_key_nums.append(num)
not_key_nums.sort(reverse=True, key=lambda x:int(x))
print(' '.join(not_key_nums))