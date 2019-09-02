# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/25 21:29'

from collections import Counter
import re

sentence = input()
sentence = sorted(re.sub('[^a-zA-Z]', '', sentence).lower())
result = Counter(sentence).most_common(1)[0]
print('%s %s' % (result[0], str(result[1])))
# print(xiaoxie)
# print(daxie)
# if xiaoxie[1] > daxie[1]:
#     print(xiaoxie[0])
# elif daxie[1] > xiaoxie[1]:
#     print(daxie[0])
# else:
#     if ord(xiaoxie[0]-daxie[0]) < 26:
#         print(daxie[0])
#     else:
#         print(xiaoxie[0])
# print(list(map(ord, sentence)))