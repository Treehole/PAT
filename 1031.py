# _*_ coding: utf-8 _*_
__author__ = 'Treehole'
__date__ = '2019/5/15 23:06'

wrong = []
weights = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
check_num = {0:'1', 1:'0', 2:'X', 3:'9', 4:'8', 5:'7', 6:'6', 7:'5', 8:'4', 9:'3', 10:'2' }
id_counts = int(input())
for i in range(id_counts):
    try:
        person_id = input()
        total = 0
        for j in range(17):
            total +=  int(person_id[j])*weights[j]
        remainder = total - 11*(total//11)
        if check_num[remainder] != person_id[-1]:
            wrong.append(person_id)
            result = False
    except:
        wrong.append(person_id)
        result = False
if wrong:
    for i in wrong:
        print(i)
else:
    print('All passed')