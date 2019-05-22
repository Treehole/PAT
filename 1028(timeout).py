# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/22 22:40'

from datetime import datetime
from operator import itemgetter

n = int(input())
results = []
today = datetime.strptime('2014/09/06', '%Y/%m/%d')
late_day = datetime.strptime('1814/09/06', '%Y/%m/%d')
for i in range(n):
    name, birthday = input().split()
    new_birthday = datetime.strptime(birthday, '%Y/%m/%d')
    if new_birthday>=late_day and new_birthday<=today:
        results.append([name, new_birthday])
new_results = sorted(results, key=itemgetter(1))
if new_results == []:
    print('0')
else:
    print('%s %s %s' % (str(len(new_results)), new_results[0][0], new_results[-1][0]))