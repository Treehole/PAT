# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/13 20:17'

num = input()
sum = 0
for i in list(num):
  sum += int(i)
pinyin = {
  '0':'ling',
  '1':'yi',
  '2':'er',
  '3':'san',
  '4':'si',
  '5':'wu',
  '6':'liu',
  '7':'qi',
  '8':'ba',
  '9':'jiu'
}
sum_list = list(str(sum))
result = ''
for i in sum_list:
  result = result + pinyin[i] + ' '
print(result.strip())