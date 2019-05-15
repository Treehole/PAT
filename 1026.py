# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/15 22:49'

start, end = input().split()
difference = int(end) - int(start)
seconds = round(difference/100)
print(seconds)
hours = seconds // 3600
minutes = (seconds - 3600*hours) // 60
second = seconds - 3600*hours - 60*minutes
print('{0}:{1}:{2}'.format(str(hours).zfill(2), str(minutes).zfill(2), str(second).zfill(2)))