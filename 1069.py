# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/7/26 22:30'

zongliang, jiange, diyiwei = input().split()
zhongjiang = []
zhuanfa = []
for i in range(int(zongliang)):
    zhuanfa.append(input())
if int(diyiwei) > int(zongliang):
    print('Keep going...')
else:
    try:
        zhongjiang.append(zhuanfa[int(diyiwei)-1])
        next = int(diyiwei)-1 + int(jiange)
        while next <= int(zongliang)-1:
            while zhuanfa[next] in zhongjiang:
                next += 1;
            if next <= int(zongliang)-1:
                zhongjiang.append(zhuanfa[next])
                next = next + int(jiange)
    except:
        pass
    for i in zhongjiang:
        print(i)